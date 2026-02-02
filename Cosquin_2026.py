import streamlit as st
import pandas as pd

st.set_page_config(page_title="Matrix CR2026 - 60min", layout="wide")

# --- DATA CON DURACIÓN DE 60 MINUTOS ---
# Se define el inicio y el fin (inicio + 1h) para dimensionar el solapamiento
data_cr = [
    # DÍA 1
    {"Día": 1, "Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "Microtul", "La Casita del Blues": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "Bersuit (15:50)", "Boomerang": "Girl Ultra", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "M. Bertoldi (17:10)", "Boomerang": "Hnos. Gutiérrez (17:20)", "La Casita del Blues": "Perro Suizo"},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "Ciro (19:40)", "Montaña": "El Kuelgue (18:40)", "Boomerang": "Estelares (19:20)", "La Casita del Blues": "Tango & Roll"},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasónicos", "Sur": "La Vela Puerca (21:40)", "Montaña": "Cuarteto de Nos (20:40)", "Boomerang": "Abel Pintos (20:40)", "La Casita del Blues": "Los Espíritus"},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "Franz Ferdinand (22:40)", "Boomerang": "Coti (23:10)", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas", "Montaña": "Chemical Bros (00:00)", "Boomerang": "", "La Casita del Blues": ""},
    # DÍA 2
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "Ainda (14:20)", "Montaña": "Renzo Leali", "Paraguay": "Wanda Jael (14:20)", "La Casita del Blues": "Rosy Gomeez"},
    {"Día": 2, "Horario": "15:20", "Norte": "Blair", "Sur": "Kapanga (15:10)", "Montaña": "Beats Modernos (15:00)", "Paraguay": "T&K (15:10)", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "Pappo x Juanse (16:25)", "Montaña": "Gustavo Cordera (15:50)", "Paraguay": "Malandro (16:10)", "La Casita del Blues": "Rudy (15:55)"},
    {"Día": 2, "Horario": "17:50", "Norte": "Bandalos Chinos", "Sur": "Plan de la Mariposa (17:45)", "Montaña": "Pericos (17:00)", "Paraguay": "Gauchos (17:20)", "La Casita del Blues": "Cordelia"},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Páez", "Sur": "Divididos (19:40)", "Montaña": "Silvestre (18:30)", "Paraguay": "Devendra (18:20)", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "20:55", "Norte": "Airbag", "Sur": "Trueno (21:30)", "Montaña": "Morat (20:20)", "Paraguay": "Marky Ramone (20:30)", "La Casita del Blues": "Crystal Thomas"},
    {"Día": 2, "Horario": "23:00", "Norte": "YSY A", "Sur": "Guasones (23:10)", "Montaña": "Pastillas (22:20)", "Paraguay": "Ellefson (21:35)", "La Casita del Blues": "Xime Monzón"},
    {"Día": 2, "Horario": "00:20", "Norte": "Caras Extrañas", "Sur": "Louta (00:50)", "Montaña": "Peces Raros (00:00)", "Paraguay": "Club Serpiente (00:45)", "La Casita del Blues": ""}
]

st.title("🎸 Matrix CR2026 - Estimador de 60 min")
st.write("Cada banda seleccionada ocupa un rango de 1 hora desde su inicio oficial.")

dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2], format_func=lambda x: f"Día {x}")

# --- FILTRADO ---
df_full = pd.DataFrame(data_cr)
df_dia = df_full[df_full["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)
escenarios = [c for c in df_dia.columns if c != "Horario"]

# --- MATRIZ INTERACTIVA ---
st.subheader("🛠️ Panel de Selección")
st.info("Hacé doble clic en el nombre de la banda para marcarla (ej: 'Lali *').")

# La matriz única donde el usuario marca directamente
matriz_editable = st.data_editor(
    df_dia,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Horario": st.column_config.TextColumn("⏰ Inicio", disabled=True),
        **{esc: st.column_config.TextColumn(disabled=False) for esc in escenarios}
    }
)

st.divider()
st.subheader("📸 Grilla Final para Captura")
st.write("Esta es tu selección final. Si hay dos bandas a la misma hora o con menos de 1h de diferencia, se solaparán.")

# Mostramos la misma matriz pero con un estilo más limpio para el Screenshot
st.dataframe(matriz_editable, hide_index=True, use_container_width=True)

st.caption("Nota: Los horarios corresponden al inicio de cada show. Se estima una duración de 60 minutos por artista para fines de planificación.")
