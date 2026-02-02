import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Matrix CR2026 Final", layout="wide")

# --- DATA COMPLETA EXTRAÍDA DE TUS IMÁGENES ---
raw_data = [
    # DÍA 1
    {"Día": 1, "H": "14:15", "Esc": "Montaña", "Art": "Chechi de Marcos"},
    {"Día": 1, "H": "14:15", "Esc": "La Casita del Blues", "Art": "Golo's Band"},
    {"Día": 1, "H": "14:30", "Esc": "Norte", "Art": "Kill Flora"},
    {"Día": 1, "H": "14:30", "Esc": "Sur", "Art": "Fantasmagoría"},
    {"Día": 1, "H": "15:20", "Esc": "Norte", "Art": "Eruca Sativa"},
    {"Día": 1, "H": "15:20", "Esc": "Sur", "Art": "La Mississippi"},
    {"Día": 1, "H": "16:30", "Esc": "Norte", "Art": "El Zar"},
    {"Día": 1, "H": "16:30", "Esc": "Sur", "Art": "Emi"},
    {"Día": 1, "H": "17:50", "Esc": "Norte", "Art": "Turf"},
    {"Día": 1, "H": "17:50", "Esc": "Sur", "Art": "Cruzando el Charco"},
    {"Día": 1, "H": "19:30", "Esc": "Norte", "Art": "Dillom"},
    {"Día": 1, "H": "19:40", "Esc": "Sur", "Art": "Ciro y Los Persas"},
    {"Día": 1, "H": "20:40", "Esc": "Montaña", "Art": "Cuarteto de Nos"},
    {"Día": 1, "H": "21:20", "Esc": "Norte", "Art": "Babasónicos"},
    {"Día": 1, "H": "21:40", "Esc": "Sur", "Art": "La Vela Puerca"},
    {"Día": 1, "H": "23:20", "Esc": "Norte", "Art": "Lali"},
    {"Día": 1, "H": "23:20", "Esc": "Sur", "Art": "Las Pelotas"},
    {"Día": 1, "H": "00:00", "Esc": "Montaña", "Art": "The Chemical Brothers"},
    {"Día": 1, "H": "00:40", "Esc": "Norte", "Art": "Caligaris"},
    {"Día": 1, "H": "00:40", "Esc": "Sur", "Art": "Viejas Locas"},
    # DÍA 2
    {"Día": 2, "H": "14:30", "Esc": "Norte", "Art": "Sofi Mora"},
    {"Día": 2, "H": "15:10", "Esc": "Sur", "Art": "Kapanga"},
    {"Día": 2, "H": "16:30", "Esc": "Norte", "Art": "Gauchito Club"},
    {"Día": 2, "H": "17:50", "Esc": "Norte", "Art": "Bandalos Chinos"},
    {"Día": 2, "H": "19:10", "Esc": "Norte", "Art": "Fito Páez"},
    {"Día": 2, "H": "19:40", "Esc": "Sur", "Art": "Divididos"},
    {"Día": 2, "H": "20:55", "Esc": "Norte", "Art": "Airbag"},
    {"Día": 2, "H": "21:30", "Esc": "Sur", "Art": "Trueno"},
    {"Día": 2, "H": "23:00", "Esc": "Norte", "Art": "YSY A"},
]

# --- FUNCIONES DE APOYO ---
def generar_bloques():
    tiempos = []
    for h in range(14, 27):
        for m in [0, 10, 20, 30, 40, 50]:
            dh = h if h < 24 else h - 24
            tiempos.append(f"{dh:02d}:{m:02d}")
    return tiempos

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=True, sheet_name='MiGrilla')
    return output.getvalue()

# --- INTERFAZ ---
st.title("🎸 Matrix CR2026 - Generador de Imagen")
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2], format_func=lambda x: f"Día {x}")

# Construcción de la matriz
tiempos = generar_bloques()
escenarios = ["Norte", "Sur", "Montaña", "Boomerang", "Paraguay", "La Casita del Blues"]
matrix_df = pd.DataFrame("", index=tiempos, columns=escenarios)

for item in raw_data:
    if item["Día"] == dia_sel:
        if item["H"] in matrix_df.index:
            matrix_df.at[item["H"], item["Esc"]] = item["Art"]

# Solo mostramos filas con contenido para que sea más corta
matrix_df = matrix_df.loc[(matrix_df != "").any(axis=1)]

st.subheader("1. Marcá tus bandas")
st.write("Editá las celdas directamente (poné un '*' al nombre) para destacar tu elección.")
edited_matrix = st.data_editor(matrix_df, use_container_width=True, height=600)

# --- EXPORTACIÓN ---
st.divider()
st.subheader("2. Descargar para el Celular")

col1, col2 = st.columns(2)

with col1:
    excel_file = to_excel(edited_matrix)
    st.download_button(
        label="📥 Descargar Grilla (Excel)",
        data=excel_file,
        file_name=f"CosquinRock_Dia{dia_sel}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

with col2:
    # Generamos una versión HTML apta para "Guardar como imagen" o PDF
    html = edited_matrix.to_html(classes='table table-striped')
    st.download_button(
        label="📄 Descargar versión HTML (Web)",
        data=html,
        file_name=f"Grilla_Dia{dia_sel}.html",
        mime="text/html"
    )

st.info("💡 **Consejo para la captura:** Si la grilla es muy larga, descarga el Excel, ábrelo en tu móvil y dale a 'Exportar a PDF' o 'Captura de pantalla de página completa'.")
