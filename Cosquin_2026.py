import streamlit as st
import pandas as pd

st.set_page_config(page_title="Matrix CR2026", layout="wide")

# --- DATA UNIFICADA (Día 1 y 2) ---
data_cr = [
    # DÍA 1
    {"Día": 1, "Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "", "La Casita del Blues": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "", "Boomerang": "Girl Ultra", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "Hnos. Gutiérrez", "La Casita del Blues": "Perro Suizo"},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "20:40", "Norte": "", "Sur": "", "Montaña": "Cuarteto de Nos", "Boomerang": "Abel Pintos", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasónicos", "Sur": "", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "21:40", "Norte": "", "Sur": "La Vela Puerca", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "", "Boomerang": "Coti", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas", "Montaña": "Chemical Bros", "Boomerang": "", "La Casita del Blues": ""},
    # DÍA 2
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "", "Montaña": "Renzo Leali", "Boomerang": "", "La Casita del Blues": "Rosy Gomeez"},
    {"Día": 2, "Horario": "15:10", "Norte": "", "Sur": "Kapanga", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "Pappo x Juanse", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "17:50", "Norte": "Bandalos Chinos", "Sur": "El Plan de la Mariposa", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Páez", "Sur": "Divididos", "Montaña": "Nicki Nicole", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "21:30", "Norte": "Los Piojos", "Sur": "Trueno", "Montaña": "Deadmau5", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "23:00", "Norte": "YSY A", "Sur": "Guasones", "Montaña": "Peces Raros", "Boomerang": "", "La Casita del Blues": ""},
]

st.title("🎸 Matrix Interactiva Cosquín Rock 2026")

# 1. Selección de Día
dia_sel = st.sidebar.radio("Día", [1, 2], format_func=lambda x: f"Día {x}")
df_dia = pd.DataFrame(data_cr)
df_dia = df_dia[df_dia["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)
escenarios = [c for c in df_dia.columns if c != "Horario"]

# 2. Matriz de Selección (Solución al nombre que no salía)
st.subheader("✅ 1. Seleccioná haciendo clic en el nombre")
st.info("Para elegir a un artista, hacé clic en el casillero de su columna. Verás su nombre arriba para no perderte.")

# Creamos una matriz de "Checks" que muestra el nombre del artista como ayuda visual
# Usamos un truco: la columna es el escenario, la fila la hora.
check_matrix = df_dia.copy()
for esc in escenarios:
    # Si hay artista, permitimos seleccionar; si no, dejamos vacío
    check_matrix[esc] = False 

# Mostramos la matriz de selección
# Ponemos la grilla de nombres como REFERENCIA estática arriba
st.write("**Grilla de Referencia (Nombres):**")
st.dataframe(df_dia, hide_index=True, use_container_width=True)

st.write("**Panel de Selección (Clic para marcar):**")
# El editor ahora solo maneja los Clics
edited_selection = st.data_editor(
    check_matrix,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Horario": st.column_config.TextColumn(disabled=True),
        **{esc: st.column_config.CheckboxColumn(label=esc) for esc in escenarios}
    }
)

# 3. Construir Resultado Final
itinerario = []
for idx, row in edited_selection.iterrows():
    for esc in escenarios:
        if row[esc]: # Si el usuario marcó el check
            nombre_artista = df_dia.iloc[idx][esc]
            if nombre_artista: # Si realmente hay alguien tocando ahí
                itinerario.append({"Hora": row["Horario"], "Escenario": esc, "Artista": nombre_artista})

# 4. Mostrar Matriz de Resultado e Imagen
if itinerario:
    st.divider()
    st.subheader("📋 2. Tu Matriz Personalizada")
    
    res_df = pd.DataFrame(itinerario)
    # Pivotamos para que el resultado sea una MATRIZ por escenario
    matriz_resultado = res_df.pivot(index="Hora", columns="Escenario", values="Artista").fillna("-")
    
    # Mostramos la tabla final prolija
    st.table(matriz_resultado)
    
    st.success("📸 ¡Listo! Sacale una captura (Screenshot) para guardarlo en tu galería.")
else:
    st.warning("Hacé clic en los casilleros del panel de selección para ver tu itinerario aquí.")
