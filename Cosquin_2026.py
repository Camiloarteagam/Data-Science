import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Matrix CR2026", layout="wide")

# --- FUNCION PARA GENERAR RANGOS DE TIEMPO REALES ---
def generar_bloques_tiempo():
    # Creamos una lista de tiempos desde las 14:00 hasta las 02:00 del día siguiente
    horas = []
    for h in range(14, 27): # Hasta las 26 para cubrir la madrugada
        for m in [0, 10, 20, 30, 40, 50]:
            display_h = h if h < 24 else h - 24
            horas.append(f"{display_h:02d}:{m:02d}")
    return horas

# --- DATA UNIFICADA (Día 1 y 2) ---
# Se organizan por su hora exacta de inicio para que el código los ubique solos
raw_data = [
    # DIA 1
    {"Día": 1, "Horario": "14:10", "Escenario": "Boomerang", "Artista": "Microtul"},
    {"Día": 1, "Horario": "14:15", "Escenario": "Montaña", "Artista": "Chechi de Marcos"},
    {"Día": 1, "Horario": "14:15", "Escenario": "La Casita del Blues", "Artista": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Escenario": "Norte", "Artista": "Kill Flora"},
    {"Día": 1, "Horario": "14:30", "Escenario": "Sur", "Artista": "Fantasmagoría"},
    {"Día": 1, "Horario": "14:50", "Escenario": "Boomerang", "Artista": "1915"},
    {"Día": 1, "Horario": "15:20", "Escenario": "Norte", "Artista": "Eruca Sativa"},
    {"Día": 1, "Horario": "15:20", "Escenario": "Sur", "Artista": "La Mississippi"},
    {"Día": 1, "Horario": "15:50", "Escenario": "Montaña", "Artista": "Bersuit Vergarabat"},
    {"Día": 1, "Horario": "16:30", "Escenario": "Norte", "Artista": "El Zar"},
    {"Día": 1, "Horario": "16:30", "Escenario": "Sur", "Artista": "Emi"},
    {"Día": 1, "Horario": "17:50", "Escenario": "Norte", "Artista": "Turf"},
    {"Día": 1, "Horario": "17:50", "Escenario": "Sur", "Artista": "Cruzando el Charco"},
    {"Día": 1, "Horario": "19:30", "Escenario": "Norte", "Artista": "Dillom"},
    {"Día": 1, "Horario": "19:40", "Escenario": "Sur", "Artista": "Ciro y Los Persas"},
    {"Día": 1, "Horario": "20:40", "Escenario": "Montaña", "Artista": "Cuarteto de Nos"},
    {"Día": 1, "Horario": "20:40", "Escenario": "Boomerang", "Artista": "Abel Pintos"},
    {"Día": 1, "Horario": "21:20", "Escenario": "Norte", "Artista": "Babasónicos"},
    {"Día": 1, "Horario": "21:40", "Escenario": "Sur", "Artista": "La Vela Puerca"},
    {"Día": 1, "Horario": "23:20", "Escenario": "Norte", "Artista": "Lali"},
    {"Día": 1, "Horario": "23:20", "Escenario": "Sur", "Artista": "Las Pelotas"},
    {"Día": 1, "Horario": "00:00", "Escenario": "Montaña", "Artista": "Chemical Bros"},
    {"Día": 1, "Horario": "00:40", "Escenario": "Sur", "Artista": "Viejas Locas"},
    # DIA 2
    {"Día": 2, "Horario": "14:20", "Escenario": "Sur", "Artista": "Ainda"},
    {"Día": 2, "Horario": "14:30", "Escenario": "Norte", "Artista": "Sofi Mora"},
    {"Día": 2, "Horario": "16:25", "Escenario": "Sur", "Artista": "Pappo x Juanse"},
    {"Día": 2, "Horario": "16:30", "Escenario": "Norte", "Artista": "Gauchito Club"},
    {"Día": 2, "Horario": "19:10", "Escenario": "Norte", "Artista": "Fito Páez"},
    {"Día": 2, "Horario": "19:40", "Escenario": "Sur", "Artista": "Divididos"},
    {"Día": 2, "Horario": "21:30", "Escenario": "Sur", "Artista": "Trueno"},
    {"Día": 2, "Horario": "20:55", "Escenario": "Norte", "Artista": "Airbag"},
]

st.title("🎸 Matrix Profesional Cosquín Rock 2026")
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2])

# --- CONSTRUCCION DE LA MATRIZ EXTENDIDA ---
bloques = generar_bloques_tiempo()
escenarios = ["Norte", "Sur", "Montaña", "Boomerang", "La Casita del Blues", "Paraguay"]

# Crear matriz vacía
matrix_df = pd.DataFrame("", index=bloques, columns=escenarios)

# Llenar matriz con la data
for item in raw_data:
    if item["Día"] == dia_sel:
        # Ubicar al artista en su horario exacto
        if item["Horario"] in matrix_df.index:
            matrix_df.at[item["Horario"], item["Escenario"]] = item["Artista"]

# Filtrar filas vacías para que la tabla no sea infinita (solo mostrar donde hay shows)
# Pero mantenemos el orden cronológico
matrix_df = matrix_df.loc[(matrix_df != "").any(axis=1)]

st.subheader(f"📅 Grilla Interactiva - Día {dia_sel}")
st.write("Doble clic en el nombre para marcarlo con un '*' o 'OK'.")

# --- FRONT END: LA MATRIZ ---
edited_matrix = st.data_editor(
    matrix_df,
    use_container_width=True,
    height=600,
    column_config={
        "index": st.column_config.TextColumn("Horario", disabled=True),
    }
)

st.success("📸 **¡Lista para captura!** Esta matriz respeta los desfasajes de tiempo (ej: 19:30 y 19:40 ya no están en la misma línea).")

st.markdown("""
<style>
    [data-testid="stTable"] { font-size: 12px; }
    .stDataFrame { border: 1px solid #4B0082; }
</style>
""", unsafe_allow_html=True)
