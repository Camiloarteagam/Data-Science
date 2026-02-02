import streamlit as st
import pandas as pd

st.set_page_config(page_title="Matrix CR2026 Final", layout="wide")

# --- GENERADOR DE BLOQUES DE TIEMPO ---
def generar_tiempos():
    tiempos = []
    for h in range(14, 27): # De 14:00 a 02:00
        for m in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]:
            dh = h if h < 24 else h - 24
            tiempos.append(f"{dh:02d}:{m:02d}")
    return tiempos

# --- DATA COMPLETA (Día 1 y 2) ---
raw_data = [
    # DÍA 1 - SÁBADO 14
    {"Día": 1, "H": "14:10", "Esc": "Boomerang", "Art": "Microtul"},
    {"Día": 1, "H": "14:15", "Esc": "Montaña", "Art": "Chechi de Marcos"},
    {"Día": 1, "H": "14:15", "Esc": "La Casita del Blues", "Art": "Golo's Band"},
    {"Día": 1, "H": "14:30", "Esc": "Norte", "Art": "Kill Flora"},
    {"Día": 1, "H": "14:30", "Esc": "Sur", "Art": "Fantasmagoría"},
    {"Día": 1, "H": "14:50", "Esc": "Boomerang", "Art": "1915"},
    {"Día": 1, "H": "15:00", "Esc": "Montaña", "Art": "Ryan"},
    {"Día": 1, "H": "15:05", "Esc": "La Casita del Blues", "Art": "Los Mentidores"},
    {"Día": 1, "H": "15:20", "Esc": "Norte", "Art": "Eruca Sativa"},
    {"Día": 1, "H": "15:20", "Esc": "Sur", "Art": "La Mississippi"},
    {"Día": 1, "H": "15:40", "Esc": "Boomerang", "Art": "Un Muerto Mas"},
    {"Día": 1, "H": "15:50", "Esc": "Montaña", "Art": "Bersuit Vergarabat"},
    {"Día": 1, "H": "15:55", "Esc": "La Casita del Blues", "Art": "Las Witches"},
    {"Día": 1, "H": "16:30", "Esc": "Norte", "Art": "El Zar"},
    {"Día": 1, "H": "16:30", "Esc": "Sur", "Art": "Emi"},
    {"Día": 1, "H": "16:30", "Esc": "Boomerang", "Art": "Girl Ultra"},
    {"Día": 1, "H": "16:50", "Esc": "La Casita del Blues", "Art": "Le Dracs"},
    {"Día": 1, "H": "17:10", "Esc": "Montaña", "Art": "Marilina Bertoldi"},
    {"Día": 1, "H": "17:20", "Esc": "Boomerang", "Art": "Hnos. Gutiérrez"},
    {"Día": 1, "H": "17:45", "Esc": "La Casita del Blues", "Art": "Perro Suizo"},
    {"Día": 1, "H": "17:50", "Esc": "Norte", "Art": "Turf"},
    {"Día": 1, "H": "17:50", "Esc": "Sur", "Art": "Cruzando el Charco"},
    {"Día": 1, "H": "18:20", "Esc": "Boomerang", "Art": "Indios"},
    {"Día": 1, "H": "18:40", "Esc": "Montaña", "Art": "El Kuelgue"},
    {"Día": 1, "H": "18:40", "Esc": "La Casita del Blues", "Art": "Misty Soul Choir"},
    {"Día": 1, "H": "19:20", "Esc": "Boomerang", "Art": "Estelares"},
    {"Día": 1, "H": "19:30", "Esc": "Norte", "Art": "Dillom"},
    {"Día": 1, "H": "19:35", "Esc": "La Casita del Blues", "Art": "Tango & Roll"},
    {"Día": 1, "H": "19:40", "Esc": "Sur", "Art": "Ciro y Los Persas"},
    {"Día": 1, "H": "20:30", "Esc": "La Casita del Blues", "Art": "Wayra Iglesias"},
    {"Día": 1, "H": "20:40", "Esc": "Montaña", "Art": "Cuarteto de Nos"},
    {"Día": 1, "H": "20:40", "Esc": "Boomerang", "Art": "Abel Pintos"},
    {"Día": 1, "H": "21:20", "Esc": "Norte", "Art": "Babasónicos"},
    {"Día": 1, "H": "21:25", "Esc": "La Casita del Blues", "Art": "Los Espíritus"},
    {"Día": 1, "H": "21:40", "Esc": "Sur", "Art": "La Vela Puerca"},
    {"Día": 1, "H": "21:50", "Esc": "Boomerang", "Art": "La Franela"},
    {"Día": 1, "H": "22:30", "Esc": "La Casita del Blues", "Art": "Piti Fernández"},
    {"Día": 1, "H": "22:40", "Esc": "Montaña", "Art": "Franz Ferdinand"},
    {"Día": 1, "H": "23:10", "Esc": "Boomerang", "Art": "Coti"},
    {"Día": 1, "H": "23:20", "Esc": "Norte", "Art": "Lali"},
    {"Día": 1, "H": "23:20", "Esc": "Sur", "Art": "Las Pelotas"},
    {"Día": 1, "H": "00:00", "Esc": "Montaña", "Art": "Chemical Bros"},
    {"Día": 1, "H": "00:40", "Esc": "Norte", "Art": "Caligaris"},
    {"Día": 1, "H": "00:40", "Esc": "Sur", "Art": "Viejas Locas"},

    # DÍA 2 - DOMINGO 15
    {"Día": 2, "H": "14:15", "Esc": "La Casita del Blues", "Art": "Rosy Gomeez"},
    {"Día": 2, "H": "14:20", "Esc": "Sur", "Art": "Ainda"},
    {"Día": 2, "H": "14:20", "Esc": "Paraguay", "Art": "Wanda Jael"},
    {"Día": 2, "H": "14:30", "Esc": "Norte", "Art": "Sofi Mora"},
    {"Día": 2, "H": "14:30", "Esc": "Montaña", "Art": "Renzo Leali"},
    {"Día": 2, "H": "15:00", "Esc": "Montaña", "Art": "Beats Modernos"},
    {"Día": 2, "H": "15:10", "Esc": "Sur", "Art": "Kapanga"},
    {"Día": 2, "H": "15:10", "Esc": "Paraguay", "Art": "T&K"},
    {"Día": 2, "H": "15:20", "Esc": "Norte", "Art": "Blair"},
    {"Día": 2, "H": "15:50", "Esc": "Montaña", "Art": "Gustavo Cordera"},
    {"Día": 2, "H": "16:10", "Esc": "Paraguay", "Art": "Malandro"},
    {"Día": 2, "H": "16:25", "Esc": "Sur", "Art": "Pappo x Juanse"},
    {"Día": 2, "H": "16:30", "Esc": "Norte", "Art": "Gauchito Club"},
    {"Día": 2, "H": "17:00", "Esc": "Montaña", "Art": "Los Pericos"},
    {"Día": 2, "H": "17:20", "Esc": "Paraguay", "Art": "Gauchos of the Pampa"},
    {"Día": 2, "H": "17:45", "Esc": "Sur", "Art": "El Plan de la Mariposa"},
    {"Día": 2, "H": "17:50", "Esc": "Norte", "Art": "Bándalos Chinos"},
    {"Día": 2, "H": "18:20", "Esc": "Paraguay", "Art": "Devendra Banhart"},
    {"Día": 2, "H": "18:30", "Esc": "Montaña", "Art": "Silvestre y La Naranja"},
    {"Día": 2, "H": "19:10", "Esc": "Norte", "Art": "Fito Páez"},
    {"Día": 2, "H": "19:30", "Esc": "Paraguay", "Art": "Dum Chica"},
    {"Día": 2, "H": "19:40", "Esc": "Sur", "Art": "Divididos"},
    {"Día": 2, "H": "20:20", "Esc": "Montaña", "Art": "Morat"},
    {"Día": 2, "H": "20:30", "Esc": "Paraguay", "Art": "Marky Ramone"},
    {"Día": 2, "H": "20:55", "Esc": "Norte", "Art": "Airbag"},
    {"Día": 2, "H": "21:30", "Esc": "Sur", "Art": "Trueno"},
    {"Día": 2, "H": "21:35", "Esc": "Paraguay", "Art": "David Ellefson"},
    {"Día": 2, "H": "22:20", "Esc": "Montaña", "Art": "Las Pastillas del Abuelo"},
    {"Día": 2, "H": "23:00", "Esc": "Norte", "Art": "YSY A"},
    {"Día": 2, "H": "23:10", "Esc": "Sur", "Art": "Guasones"},
    {"Día": 2, "H": "00:00", "Esc": "Montaña", "Art": "Peces Raros"},
    {"Día": 2, "H": "00:20", "Esc": "Norte", "Art": "Caras Extrañas"},
    {"Día": 2, "H": "00:45", "Esc": "Paraguay", "Art": "Club de la Serpiente"},
    {"Día": 2, "H": "00:50", "Esc": "Sur", "Art": "Louta"},
]

st.title("Cosquín Rock 2026")
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2], format_func=lambda x: f"Día {x}")

# --- CONSTRUCCIÓN DE MATRIZ ---
tiempos = generar_tiempos()
escenarios = ["Norte", "Sur", "Montaña", "Boomerang", "Paraguay", "La Casita del Blues"]
matrix_df = pd.DataFrame("", index=tiempos, columns=escenarios)

for item in raw_data:
    if item["Día"] == dia_sel:
        if item["H"] in matrix_df.index:
            matrix_df.at[item["H"], item["Esc"]] = item["Art"]

# Filtrar solo filas con artistas
matrix_df = matrix_df.loc[(matrix_df != "").any(axis=1)]

# --- FRONT END ---
st.subheader(f"Día {dia_sel}")
st.write("Escribí '*' o 'OK' al lado del nombre para marcar tus bandas. Los horarios respetan los desfasajes exactos.")

st.data_editor(
    matrix_df,
    use_container_width=True,
    height=800,
    column_config={"index": st.column_config.TextColumn("Horario", disabled=True)}
)

st.success("📸 **¡Lista para captura!** Todos los escenarios están incluidos con sus horarios reales.")
