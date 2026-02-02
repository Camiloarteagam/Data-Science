import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simulador Cosquín Rock 2026", layout="wide")

# --- DATA OFICIAL (Sábado 14 y Domingo 15) ---
data_cr = [
    # DÍA 1
    {"Día": 1, "Horario": "14:15", "Escenarios": "M: Chechi de Marcos | B: Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Escenarios": "N: Kill Flora | S: Fantasmagoría"},
    {"Día": 1, "Horario": "15:20", "Escenarios": "N: Eruca Sativa | S: La Mississippi"},
    {"Día": 1, "Horario": "16:30", "Escenarios": "N: El Zar | S: Emi | B: Girl Ultra"},
    {"Día": 1, "Horario": "17:50", "Escenarios": "N: Turf | S: Cruzando el Charco"},
    {"Día": 1, "Horario": "19:30", "Escenarios": "N: Dillom"},
    {"Día": 1, "Horario": "19:40", "Escenarios": "S: Ciro y Los Persas"},
    {"Día": 1, "Horario": "20:40", "Escenarios": "M: Cuarteto de Nos | B: Abel Pintos"},
    {"Día": 1, "Horario": "21:20", "Escenarios": "N: Babasónicos"},
    {"Día": 1, "Horario": "21:40", "Escenarios": "S: La Vela Puerca"},
    {"Día": 1, "Horario": "22:40", "Escenarios": "M: Franz Ferdinand"},
    {"Día": 1, "Horario": "23:20", "Escenarios": "N: Lali | S: Las Pelotas"},
    {"Día": 1, "Horario": "00:00", "Escenarios": "M: The Chemical Brothers"},
    {"Día": 1, "Horario": "00:40", "Escenarios": "N: Caligaris | S: Viejas Locas"},
    # DÍA 2
    {"Día": 2, "Horario": "14:30", "Escenarios": "N: Sofi Mora | M: Renzo Leali"},
    {"Día": 2, "Horario": "15:10", "Escenarios": "S: Kapanga | P: T&K"},
    {"Día": 2, "Horario": "16:30", "Escenarios": "N: Gauchito Club"},
    {"Día": 2, "Horario": "17:45", "Escenarios": "S: El Plan de la Mariposa"},
    {"Día": 2, "Horario": "17:50", "Escenarios": "N: Bándalos Chinos"},
    {"Día": 2, "Horario": "19:10", "Escenarios": "N: Fito Páez"},
    {"Día": 2, "Horario": "19:40", "Escenarios": "S: Divididos | M: Nicki Nicole"},
    {"Día": 2, "Horario": "20:55", "Escenarios": "N: Airbag"},
    {"Día": 2, "Horario": "21:30", "Escenarios": "S: Trueno"},
    {"Día": 2, "Horario": "22:40", "Escenarios": "M: Deadmau5"},
    {"Día": 2, "Horario": "23:00", "Escenarios": "N: YSY A"},
    {"Día": 2, "Horario": "00:50", "Escenarios": "S: Louta"},
]

st.title("🎸 Matrix Selector CR2026")

# Selector de día
dia = st.sidebar.radio("Seleccioná el Día", [1, 2])
df = pd.DataFrame(data_cr)
df_dia = df[df["Día"] == dia][["Horario", "Escenarios"]].copy()
df_dia.insert(0, "Seleccionar", False)

st.subheader(f"Grilla Día {dia}")
st.write("Marcá el cuadrito a la izquierda de la banda que querés ver.")

# Matriz interactiva ultra-ligera
# Referencia de Escenarios: N=Norte, S=Sur, M=Montaña, B=Boomerang/Blues, P=Paraguay
edited_df = st.data_editor(
    df_dia,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Seleccionar": st.column_config.CheckboxColumn(default=False),
        "Horario": st.column_config.TextColumn(width="small", disabled=True),
        "Escenarios": st.column_config.TextColumn(disabled=True)
    }
)

# Filtrar seleccionados
itinerario = edited_df[edited_df["Seleccionar"] == True]

if not itinerario.empty:
    st.divider()
    st.subheader("📋 Tu Itinerario")
    st.table(itinerario[["Horario", "Escenarios"]])
    
    # Alerta de choques horaria
    if itinerario["Horario"].duplicated().any():
        st.warning("⚠️ Tenés bandas seleccionadas a la misma hora.")
else:
    st.info("Hacé clic en los casilleros de la columna 'Seleccionar' para armar tu ruta.")
