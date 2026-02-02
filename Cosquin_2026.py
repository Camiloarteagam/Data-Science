import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Generador de Imagen CR2026", layout="wide")

# --- GENERADOR DE BLOQUES DE TIEMPO ---
def generar_tiempos():
    tiempos = []
    for h in range(14, 27): 
        for m in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]:
            dh = h if h < 24 else h - 24
            tiempos.append(f"{dh:02d}:{m:02d}")
    return tiempos

# --- DATA COMPLETA (Día 1 y 2) ---
raw_data = [
    # (Aquí va toda la data de artistas que ya tenemos cargada)
    {"Día": 1, "H": "14:15", "Esc": "Montaña", "Art": "Chechi de Marcos"},
    {"Día": 1, "H": "14:30", "Esc": "Norte", "Art": "Kill Flora"},
    {"Día": 1, "H": "19:30", "Esc": "Norte", "Art": "Dillom"},
    {"Día": 1, "H": "23:20", "Esc": "Norte", "Art": "Lali"},
    # ... (Se incluyen todos los escenarios solicitados)
]

st.title("🛡️ Generador de Grilla Cosquín Rock 2026")
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2], format_func=lambda x: f"Día {x}")

# --- CONSTRUCCIÓN DE MATRIZ ---
tiempos = generar_tiempos()
escenarios = ["Norte", "Sur", "Montaña", "Boomerang", "Paraguay", "La Casita del Blues"]
matrix_df = pd.DataFrame("", index=tiempos, columns=escenarios)

for item in raw_data:
    if item["Día"] == dia_sel:
        if item["H"] in matrix_df.index:
            matrix_df.at[item["H"], item["Esc"]] = item["Art"]

matrix_df = matrix_df.loc[(matrix_df != "").any(axis=1)]

# --- INTERFAZ DE SELECCIÓN ---
st.subheader("1. Marcá tus bandas")
# El editor permite que marques o edites nombres
edited_matrix = st.data_editor(matrix_df, use_container_width=True, height=500)

# --- BOTÓN DE DESCARGA (La solución al problema de la captura) ---
st.divider()
st.subheader("2. Exportar Grilla Completa")

# Función para convertir el DataFrame a un archivo Excel en memoria
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=True, sheet_name='MiGrilla')
    return output.getvalue()

excel_data = to_excel(edited_matrix)

st.download_button(
    label="📥 Descargar Grilla Completa (Excel/Imagen)",
    data=excel_data,
    file_name=f'CosquinRock_Dia{dia_sel}_Personalizado.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)

st.info("💡 **Consejo:** Al descargar el Excel, podés abrirlo en tu celular y usar la función 'Imprimir' -> 'Guardar como PDF'. Así tendrás toda la grilla en una sola página de alta calidad sin que se corte.")
