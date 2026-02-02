import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simulador Cosquín Rock 2026", layout="wide")

# --- DATA OFICIAL (Extraída de tus imágenes) ---
# Día 1: Sábado 14 de Febrero
# Día 2: Domingo 15 de Febrero
data_cr = [
    {"Día": 1, "Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "Microtul", "Blues": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "14:50", "Norte": "", "Sur": "", "Montaña": "", "Boomerang": "1915", "Blues": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "", "Boomerang": "Girl Ultra", "Blues": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "20:40", "Norte": "", "Sur": "", "Montaña": "Cuarteto de Nos", "Boomerang": "Abel Pintos", "Blues": ""},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasónicos", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "21:40", "Norte": "", "Sur": "La Vela Puerca", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "00:00", "Norte": "", "Sur": "", "Montaña": "The Chemical Brothers", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas", "Montaña": "", "Boomerang": "", "Blues": ""},
    # DÍA 2
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "", "Montaña": "Renzo Leali", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "15:10", "Norte": "", "Sur": "Kapanga", "Montaña": "", "Paraguay": "T&K", "Blues": ""},
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "17:50", "Norte": "Bandalos Chinos", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Páez", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "19:40", "Norte": "", "Sur": "Divididos", "Montaña": "Nicki Nicole", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "20:55", "Norte": "Airbag", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "21:30", "Norte": "", "Sur": "Trueno", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "22:40", "Norte": "", "Sur": "", "Montaña": "Deadmau5", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "23:00", "Norte": "YSY A", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "00:50", "Norte": "", "Sur": "Louta", "Montaña": "", "Paraguay": "", "Blues": ""},
]

st.title("🎸 Matrix Selector: Cosquín Rock 2026")
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2], format_func=lambda x: f"Día {x}")

# --- PROCESAMIENTO ---
df_full = pd.DataFrame(data_cr)
df_dia = df_full[df_full["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)
escenarios = [c for c in df_dia.columns if c != "Horario"]

# Creamos la matriz de visualización donde cada celda tiene "Artista \n [ ]"
# Pero para que sea clickeable, usaremos la lógica de espejo
st.subheader("1. Consultá y marcá tu banda")
st.info("Buscá el nombre del artista en la tabla superior y marcá el casillero correspondiente en la grilla de abajo.")

# Tabla de nombres (Referencia)
st.dataframe(df_dia, hide_index=True, use_container_width=True)

# Tabla de selección (Matriz de Checkboxes)
# Inicializamos el estado de la selección si no existe
if f"picks_{dia_sel}" not in st.session_state:
    st.session_state[f"picks_{dia_sel}"] = pd.DataFrame(False, index=df_dia.index, columns=escenarios)

st.write("---")
st.write("**Grilla de Selección (Marcá aquí):**")

# Unimos Horario con los casilleros
selector_df = pd.concat([df_dia[["Horario"]], st.session_state[f"picks_{dia_sel}"]], axis=1)

edited_df = st.data_editor(
    selector_df,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Horario": st.column_config.TextColumn(disabled=True),
        **{esc: st.column_config.CheckboxColumn(label=esc) for esc in escenarios}
    }
)

# --- LÓGICA DE RESULTADO ---
itinerario = []
for idx, row in edited_df.iterrows():
    hora = row["Horario"]
    for esc in escenarios:
        if row[esc] == True:
            artista_nombre = df_dia.loc[idx, esc]
            if artista_nombre:
                itinerario.append({"Horario": hora, "Escenario": esc, "Artista": artista_nombre})

# --- MOSTRAR ITINERARIO ---
st.divider()
st.subheader("📋 Tu Itinerario Generado")

if itinerario:
    final_df = pd.DataFrame(itinerario).sort_values("Horario")
    st.table(final_df)
    
    # Detección de colisiones horarias
    if final_df["Horario"].duplicated().any():
        st.error("⚠️ ¡Cuidado! Elegiste dos artistas que tocan al mismo tiempo.")
else:
    st.write("No has seleccionado ningún artista todavía.")
