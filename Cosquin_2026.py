import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cosquín Rock 2026 - Matrix", layout="wide")

# --- DATOS OFICIALES ---
# (Se mantiene tu lista data_cr igual)
data_cr = [
    {"Día": 1, "Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "", "Blues": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "14:50", "Norte": "", "Sur": "", "Montaña": "", "Boomerang": "1915", "Blues": ""},
    {"Día": 1, "Horario": "15:00", "Norte": "", "Sur": "", "Montaña": "Ryan", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "15:50", "Norte": "", "Sur": "", "Montaña": "Bersuit Vergarabat", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "", "Boomerang": "Girl Ultra", "Blues": ""},
    {"Día": 1, "Horario": "17:10", "Norte": "", "Sur": "", "Montaña": "Marilina Bertoldi", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "18:40", "Norte": "", "Sur": "", "Montaña": "El Kuelgue", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "20:40", "Norte": "", "Sur": "", "Montaña": "Cuarteto de Nos", "Boomerang": "Abel Pintos", "Blues": ""},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasónicos", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "21:40", "Norte": "", "Sur": "La Vela Puerca", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "22:40", "Norte": "", "Sur": "", "Montaña": "Franz Ferdinand", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "00:00", "Norte": "", "Sur": "", "Montaña": "The Chemical Brothers", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas", "Montaña": "", "Boomerang": "", "Blues": ""},
    # DÍA 2
    {"Día": 2, "Horario": "14:20", "Norte": "", "Sur": "Ainda", "Montaña": "", "Paraguay": "Wanda Jael", "Blues": ""},
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "", "Montaña": "Renzo Leali", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "15:10", "Norte": "", "Sur": "Kapanga", "Montaña": "", "Paraguay": "T&K", "Blues": ""},
    {"Día": 2, "Horario": "15:20", "Norte": "Blair", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "17:45", "Norte": "", "Sur": "El Plan de la Mariposa", "Montaña": "", "Paraguay": "", "Blues": "Cordelia's Blues"},
    {"Día": 2, "Horario": "17:50", "Norte": "Bandalos Chinos", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Páez", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "19:40", "Norte": "", "Sur": "Divididos", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "20:20", "Norte": "", "Sur": "", "Montaña": "Morat", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "20:55", "Norte": "Airbag", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "21:30", "Norte": "", "Sur": "Trueno", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "22:20", "Norte": "", "Sur": "", "Montaña": "Las Pastillas del Abuelo", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "23:00", "Norte": "YSY A", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "00:00", "Norte": "", "Sur": "", "Montaña": "Peces Raros", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "00:20", "Norte": "Caras Extrañas", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "00:50", "Norte": "", "Sur": "Louta", "Montaña": "", "Paraguay": "", "Blues": ""},
]

st.title("🎸 Simulador Interactivo Cosquín Rock 2026")
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2])

# 1. Preparar el DataFrame base
df_full = pd.DataFrame(data_cr)
df_dia = df_full[df_full["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)

# 2. Crear una matriz paralela de selección (booleana)
# Esta matriz rastrea qué celdas están seleccionadas
if f"picks_{dia_sel}" not in st.session_state:
    st.session_state[f"picks_{dia_sel}"] = pd.DataFrame(False, index=df_dia.index, columns=df_dia.columns[1:])

st.subheader(f"📅 Matriz de Selección - Día {dia_sel}")
st.write("Selecciona los artistas directamente en la tabla (Haz doble clic o usa la barra espaciadora en las celdas con nombres).")

# 3. Mostrar la matriz como editor. 
# Para que el usuario vea nombres pero edite booleanos, mostramos la matriz de nombres 
# y permitimos la edición sobre ella.
edited_matrix = st.data_editor(
    df_dia,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Horario": st.column_config.TextColumn(disabled=True),
        # Configuramos las columnas de escenarios como Checkboxes que muestran el texto
        "Norte": st.column_config.CheckboxColumn(),
        "Sur": st.column_config.CheckboxColumn(),
        "Montaña": st.column_config.CheckboxColumn(),
        "Boomerang": st.column_config.CheckboxColumn(),
        "Paraguay": st.column_config.CheckboxColumn(),
        "Blues": st.column_config.CheckboxColumn(),
    }
)

st.divider()

# 4. Procesar la selección
# Comparamos la matriz original (nombres) con la editada (booleanos)
itinerario_lista = []

for row_idx in range(len(edited_matrix)):
    hora = edited_matrix.iloc[row_idx]["Horario"]
    for esc in edited_matrix.columns[1:]:
        # Si el valor en la celda es True (fue seleccionado)
        val = edited_matrix.iloc[row_idx][esc]
        if val is True:
            # Recuperamos el nombre del artista de la data original
            artista_original = df_dia.iloc[row_idx][esc]
            if artista_original != "":
                itinerario_lista.append({
                    "Horario": hora,
                    "Escenario": esc,
                    "Artista": artista_original
                })

# 5. Mostrar resultado
st.subheader("📋 Tu Itinerario Confirmado")
if itinerario_lista:
    res_df = pd.DataFrame(itinerario_lista)
    
    # Check de solapamientos
    duplicados = res_df.duplicated(subset=['Horario'], keep=False)
    
    if duplicados.any():
        st.warning("⚠️ ¡Ojo! Tienes artistas seleccionados a la misma hora.")
    
    st.table(res_df)
    
    # Botón para limpiar (opcional)
    if st.button("Limpiar Selección"):
        st.rerun()
else:
    st.info("Haz clic en los nombres de los artistas en la tabla de arriba para armar tu ruta.")
