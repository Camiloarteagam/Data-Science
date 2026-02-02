import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mi Grilla Cosquín 2026", layout="wide")

# --- BASE DE DATOS COMPLETA (Día 1 y Día 2) ---
data_cr = [
    # DÍA 1
    {"Día": 1, "Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "Microtul", "Paraguay": "", "La Casita del Blues": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "", "Boomerang": "Girl Ultra", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "Hermanos Gutiérrez", "Paraguay": "", "La Casita del Blues": "Perro Suizo"},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "Estelares (19:20)", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": "Tango & Roll"},
    {"Día": 1, "Horario": "20:40", "Norte": "", "Sur": "", "Montaña": "Cuarteto de Nos", "Boomerang": "Abel Pintos", "Paraguay": "", "La Casita del Blues": "Wayra Iglesias"},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasónicos", "Sur": "La Vela Puerca (21:40)", "Montaña": "", "Boomerang": "La Franela", "Paraguay": "", "La Casita del Blues": "Los Espíritus"},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "Franz Ferdinand (22:40)", "Boomerang": "Coti (23:10)", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas", "Montaña": "The Chemical Brothers (00:00)", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    
    # DÍA 2
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "Ainda (14:20)", "Montaña": "Renzo Leali", "Boomerang": "", "Paraguay": "Wanda Jael", "La Casita del Blues": "Rosy Gomeez"},
    {"Día": 2, "Horario": "15:10", "Norte": "Blair (15:20)", "Sur": "Kapanga", "Montaña": "Beats Modernos", "Boomerang": "", "Paraguay": "T&K", "La Casita del Blues": "Labios de Sal"},
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "Pappo x Juanse", "Montaña": "Gustavo Cordera (15:50)", "Boomerang": "", "Paraguay": "Malandro", "La Casita del Blues": "Rudy"},
    {"Día": 2, "Horario": "17:50", "Norte": "Bándalos Chinos", "Sur": "El Plan de la Mariposa (17:45)", "Montaña": "Los Pericos (17:00)", "Boomerang": "", "Paraguay": "Gauchos of the Pampa", "La Casita del Blues": "Cordelia's Blues"},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Páez", "Sur": "Divididos (19:40)", "Montaña": "Silvestre y La Naranja (18:30)", "Boomerang": "", "Paraguay": "Devendra Banhart (18:20)", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "20:55", "Norte": "Airbag", "Sur": "Trueno (21:30)", "Montaña": "Morat (20:20)", "Boomerang": "", "Paraguay": "Marky Ramone (20:30)", "La Casita del Blues": "Crystal Thomas"},
    {"Día": 2, "Horario": "23:00", "Norte": "YSY A", "Sur": "Guasones (23:10)", "Montaña": "Las Pastillas del Abuelo (22:20)", "Boomerang": "", "Paraguay": "David Ellefson (21:35)", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "00:20", "Norte": "Caras Extrañas", "Sur": "Louta (00:50)", "Montaña": "Peces Raros (00:00)", "Boomerang": "", "Paraguay": "Club de la Serpiente", "La Casita del Blues": ""}
]

st.title("🎸 Matrix Interactiva Cosquín Rock 2026")
st.write("👉 **Instrucciones:** Haz doble clic en el nombre del artista que quieras elegir y añade un `*` o escribe `OK`. Cuando termines, toma una captura de pantalla a esta tabla única.")

dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2], format_func=lambda x: f"Día {x}")

# --- FILTRADO Y PREPARACIÓN ---
df_full = pd.DataFrame(data_cr)
df_dia = df_full[df_full["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)
escenarios = [c for c in df_dia.columns if c != "Horario"]

# --- LA MATRIZ ÚNICA INTERACTIVA ---
# Configuramos para que todas las celdas de artistas sean editables directamente
st.data_editor(
    df_dia,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Horario": st.column_config.TextColumn(disabled=True),
        **{esc: st.column_config.TextColumn(disabled=False) for esc in escenarios}
    }
)

st.info("📸 **¡Listo para capturar!** Una vez marcados tus artistas arriba, ya tienes tu flyer personalizado.")

# Estilo visual para mejorar la captura
st.markdown("""
    <style>
    .stDataFrame {
        border: 2px solid #6d28d9;
        border-radius: 8px;
        padding: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
