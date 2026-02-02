import streamlit as st
import pandas as pd

st.set_page_config(page_title="Matriz Cosquín 2026", layout="wide")

# --- CARGA DE DATOS OFICIALES (DÍA 1 Y 2) ---
# Datos extraídos directamente de tus imágenes oficiales
data_cr = [
    # DÍA 1
    {"Día": "Sábado 14", "Horario": "14:15", "Escenario": "Montaña", "Artista": "Chechi de Marcos"},
    {"Día": "Sábado 14", "Horario": "14:15", "Escenario": "Blues", "Artista": "Golo's Band"},
    {"Día": "Sábado 14", "Horario": "14:30", "Escenario": "Norte", "Artista": "Kill Flora"},
    {"Día": "Sábado 14", "Horario": "14:30", "Escenario": "Sur", "Artista": "Fantasmagoría"},
    {"Día": "Sábado 14", "Horario": "15:20", "Escenario": "Norte", "Artista": "Eruca Sativa"},
    {"Día": "Sábado 14", "Horario": "15:20", "Escenario": "Sur", "Artista": "La Mississippi"},
    {"Día": "Sábado 14", "Horario": "16:30", "Escenario": "Norte", "Artista": "El Zar"},
    {"Día": "Sábado 14", "Horario": "17:10", "Escenario": "Montaña", "Artista": "Marilina Bertoldi"},
    {"Día": "Sábado 14", "Horario": "17:50", "Escenario": "Norte", "Artista": "Turf"},
    {"Día": "Sábado 14", "Horario": "17:50", "Escenario": "Sur", "Artista": "Cruzando el Charco"},
    {"Día": "Sábado 14", "Horario": "19:30", "Escenario": "Norte", "Artista": "Dillom"},
    {"Día": "Sábado 14", "Horario": "19:40", "Escenario": "Sur", "Artista": "Ciro y Los Persas"},
    {"Día": "Sábado 14", "Horario": "20:40", "Escenario": "Boomerang", "Artista": "Abel Pintos"},
    {"Día": "Sábado 14", "Horario": "20:40", "Escenario": "Montaña", "Artista": "Cuarteto de Nos"},
    {"Día": "Sábado 14", "Horario": "21:20", "Escenario": "Norte", "Artista": "Babasónicos"},
    {"Día": "Sábado 14", "Horario": "21:40", "Escenario": "Sur", "Artista": "La Vela Puerca"},
    {"Día": "Sábado 14", "Horario": "22:40", "Escenario": "Montaña", "Artista": "Franz Ferdinand"},
    {"Día": "Sábado 14", "Horario": "23:20", "Escenario": "Norte", "Artista": "Lali"},
    {"Día": "Sábado 14", "Horario": "23:20", "Escenario": "Sur", "Artista": "Las Pelotas"},
    {"Día": "Sábado 14", "Horario": "00:00", "Escenario": "Montaña", "Artista": "The Chemical Brothers"},
    {"Día": "Sábado 14", "Horario": "00:40", "Escenario": "Sur", "Artista": "Viejas Locas x Fachi y Abel"},
    
    # DÍA 2
    {"Día": "Domingo 15", "Horario": "15:10", "Escenario": "Sur", "Artista": "Kapanga"},
    {"Día": "Domingo 15", "Horario": "15:20", "Escenario": "Norte", "Artista": "Blair"},
    {"Día": "Domingo 15", "Horario": "16:25", "Escenario": "Sur", "Artista": "Pappo x Juanse"},
    {"Día": "Domingo 15", "Horario": "16:30", "Escenario": "Norte", "Artista": "Gauchito Club"},
    {"Día": "Domingo 15", "Horario": "17:00", "Escenario": "Montaña", "Artista": "Los Pericos"},
    {"Día": "Domingo 15", "Horario": "17:45", "Escenario": "Sur", "Artista": "El Plan de la Mariposa"},
    {"Día": "Domingo 15", "Horario": "17:50", "Escenario": "Norte", "Artista": "Bandalos Chinos"},
    {"Día": "Domingo 15", "Horario": "18:30", "Escenario": "Montaña", "Artista": "Silvestre y La Naranja"},
    {"Día": "Domingo 15", "Horario": "19:10", "Escenario": "Norte", "Artista": "Fito Páez"},
    {"Día": "Domingo 15", "Horario": "19:40", "Escenario": "Sur", "Artista": "Divididos"},
    {"Día": "Domingo 15", "Horario": "20:20", "Escenario": "Montaña", "Artista": "Morat"},
    {"Día": "Domingo 15", "Horario": "20:55", "Escenario": "Norte", "Artista": "Airbag"},
    {"Día": "Domingo 15", "Horario": "21:30", "Escenario": "Sur", "Artista": "Trueno"},
    {"Día": "Domingo 15", "Horario": "22:20", "Escenario": "Montaña", "Artista": "Las Pastillas del Abuelo"},
    {"Día": "Domingo 15", "Horario": "23:00", "Escenario": "Norte", "Artista": "YSY A"},
    {"Día": "Domingo 15", "Horario": "00:00", "Escenario": "Montaña", "Artista": "Peces Raros"},
    {"Día": "Domingo 15", "Horario": "00:20", "Escenario": "Norte", "Artista": "Caras Extrañas"},
    {"Día": "Domingo 15", "Horario": "00:50", "Escenario": "Sur", "Artista": "Louta"},
]

st.title("🎸 Matriz Interactiva Cosquín Rock 2026")
st.write("Pulsa en la columna **'Seleccionar'** para armar tu cronograma.")

# Selector de día
dia_filtro = st.sidebar.radio("Elige el día:", ["Sábado 14", "Domingo 15"])

# Preparar DataFrame
df = pd.DataFrame(data_cr)
df_dia = df[df["Día"] == dia_filtro].copy()
df_dia.insert(0, "Seleccionar", False)

# --- FRONT: MATRIZ PARA PULSAR ---
# Usamos data_editor que permite "pulsar" sobre los checkboxes
matriz_editada = st.data_editor(
    df_dia,
    column_config={
        "Seleccionar": st.column_config.CheckboxColumn(help="Pulsa para elegir este show"),
        "Horario": st.column_config.TextColumn(width="small"),
        "Día": None # Ocultamos la columna día para limpiar el front
    },
    disabled=["Horario", "Escenario", "Artista"],
    hide_index=True,
    use_container_width=True
)

# --- LÓGICA DE ITINERARIO ---
itinerario = matriz_editada[matriz_editada["Seleccionar"] == True].sort_values("Horario")

if not itinerario.empty:
    st.markdown("---")
    st.subheader("📋 Tu Hoja de Ruta Seleccionada")
    
    for h, grupo in itinerario.groupby("Horario"):
        with st.expander(f"⏰ {h}", expanded=True):
            for _, row in grupo.iterrows():
                if len(grupo) > 1:
                    st.error(f"⚠️ **PISADO:** {row['Artista']} en {row['Escenario']}")
                else:
                    st.success(f"✅ **{row['Artista']}** — Escenario {row['Escenario']}")
else:
    st.info("💡 Pulsa en los casilleros de la tabla superior para ver tu itinerario aquí.")
