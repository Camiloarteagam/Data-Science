import streamlit as st
import pandas as pd

# Configuración de la interfaz
st.set_page_config(page_title="Simulador CR2026", page_icon="🎸", layout="wide")

# --- BASE DE DATOS COMPLETA (Basada en tus imágenes) ---
data = [
    # DÍA 1
    {"Día": 1, "Horario": "14:15", "Escenario": "Montaña", "Artista": "Chechi de Marcos"},
    {"Día": 1, "Horario": "14:15", "Escenario": "Blues", "Artista": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Escenario": "Norte", "Artista": "Kill Flora"},
    {"Día": 1, "Horario": "14:30", "Escenario": "Sur", "Artista": "Fantasmagoría"},
    {"Día": 1, "Horario": "14:50", "Escenario": "Boomerang", "Artista": "1915"},
    {"Día": 1, "Horario": "15:00", "Escenario": "Montaña", "Artista": "Ryan"},
    {"Día": 1, "Horario": "15:20", "Escenario": "Norte", "Artista": "Eruca Sativa"},
    {"Día": 1, "Horario": "15:20", "Escenario": "Sur", "Artista": "La Mississippi"},
    {"Día": 1, "Horario": "15:50", "Escenario": "Montaña", "Artista": "Bersuit Vergarabat"},
    {"Día": 1, "Horario": "16:30", "Escenario": "Norte", "Artista": "El Zar"},
    {"Día": 1, "Horario": "16:30", "Escenario": "Sur", "Artista": "Emi"},
    {"Día": 1, "Horario": "17:10", "Escenario": "Montaña", "Artista": "Marilina Bertoldi"},
    {"Día": 1, "Horario": "17:50", "Escenario": "Norte", "Artista": "Turf"},
    {"Día": 1, "Horario": "17:50", "Escenario": "Sur", "Artista": "Cruzando el Charco"},
    {"Día": 1, "Horario": "18:40", "Escenario": "Montaña", "Artista": "El Kuelgue"},
    {"Día": 1, "Horario": "19:30", "Escenario": "Norte", "Artista": "Dillom"},
    {"Día": 1, "Horario": "19:40", "Escenario": "Sur", "Artista": "Ciro y Los Persas"},
    {"Día": 1, "Horario": "20:40", "Escenario": "Montaña", "Artista": "Cuarteto de Nos"},
    {"Día": 1, "Horario": "20:40", "Escenario": "Boomerang", "Artista": "Abel Pintos"},
    {"Día": 1, "Horario": "21:20", "Escenario": "Norte", "Artista": "Babasónicos"},
    {"Día": 1, "Horario": "21:40", "Escenario": "Sur", "Artista": "La Vela Puerca"},
    {"Día": 1, "Horario": "22:40", "Escenario": "Montaña", "Artista": "Franz Ferdinand"},
    {"Día": 1, "Horario": "23:20", "Escenario": "Norte", "Artista": "Lali"},
    {"Día": 1, "Horario": "23:20", "Escenario": "Sur", "Artista": "Las Pelotas"},
    {"Día": 1, "Horario": "00:00", "Escenario": "Montaña", "Artista": "The Chemical Brothers"},
    {"Día": 1, "Horario": "00:40", "Escenario": "Norte", "Artista": "Caligaris"},
    {"Día": 1, "Horario": "00:40", "Escenario": "Sur", "Artista": "Viejas Locas x Fachi y Abel"},
    
    # DÍA 2
    {"Día": 2, "Horario": "14:20", "Escenario": "Sur", "Artista": "Ainda"},
    {"Día": 2, "Horario": "14:20", "Escenario": "Paraguay", "Artista": "Wanda Jael"},
    {"Día": 2, "Horario": "14:30", "Escenario": "Norte", "Artista": "Sofi Mora"},
    {"Día": 2, "Horario": "14:30", "Escenario": "Montaña", "Artista": "Renzo Leali"},
    {"Día": 2, "Horario": "15:10", "Escenario": "Sur", "Artista": "Kapanga"},
    {"Día": 2, "Horario": "15:20", "Escenario": "Norte", "Artista": "Blair"},
    {"Día": 2, "Horario": "15:50", "Escenario": "Montaña", "Artista": "Gustavo Cordera"},
    {"Día": 2, "Horario": "16:25", "Escenario": "Sur", "Artista": "Pappo x Juanse"},
    {"Día": 2, "Horario": "16:30", "Escenario": "Norte", "Artista": "Gauchito Club"},
    {"Día": 2, "Horario": "17:00", "Escenario": "Montaña", "Artista": "Los Pericos"},
    {"Día": 2, "Horario": "17:45", "Escenario": "Sur", "Artista": "El Plan de la Mariposa"},
    {"Día": 2, "Horario": "17:50", "Escenario": "Norte", "Artista": "Bandalos Chinos"},
    {"Día": 2, "Horario": "18:20", "Escenario": "Paraguay", "Artista": "Devendra Banhart"},
    {"Día": 2, "Horario": "18:30", "Escenario": "Montaña", "Artista": "Silvestre y La Naranja"},
    {"Día": 2, "Horario": "19:10", "Escenario": "Norte", "Artista": "Fito Páez"},
    {"Día": 2, "Horario": "19:40", "Escenario": "Sur", "Artista": "Divididos"},
    {"Día": 2, "Horario": "20:20", "Escenario": "Montaña", "Artista": "Morat"},
    {"Día": 2, "Horario": "20:30", "Escenario": "Paraguay", "Artista": "Marky Ramone"},
    {"Día": 2, "Horario": "20:55", "Escenario": "Norte", "Artista": "Airbag"},
    {"Día": 2, "Horario": "21:30", "Escenario": "Sur", "Artista": "Trueno"},
    {"Día": 2, "Horario": "21:35", "Escenario": "Paraguay", "Artista": "David Ellefson"},
    {"Día": 2, "Horario": "22:20", "Escenario": "Montaña", "Artista": "Las Pastillas del Abuelo"},
    {"Día": 2, "Horario": "23:00", "Escenario": "Norte", "Artista": "YSY A"},
    {"Día": 2, "Horario": "23:10", "Escenario": "Sur", "Artista": "Guasones"},
    {"Día": 2, "Horario": "00:00", "Escenario": "Montaña", "Artista": "Peces Raros"},
    {"Día": 2, "Horario": "00:20", "Escenario": "Norte", "Artista": "Caras Extrañas"},
    {"Día": 2, "Horario": "00:50", "Escenario": "Sur", "Artista": "Louta"},
]

st.title("🎸 Simulador de Itinerario Cosquín Rock 2026")
st.markdown("Seleccioná tus artistas en la tabla y armá tu hoja de ruta personalizada.")

# Filtro de día
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2], format_func=lambda x: f"Día {x}")

# Procesar DataFrame
df = pd.DataFrame(data)
df_display = df[df["Día"] == dia_sel].copy()
df_display["Ir a ver"] = False # Columna para el checkbox

# --- FRONT: SELECCIÓN EN TABLA ---
st.subheader(f"Grilla Horaria - Día {dia_sel}")
# Usamos data_editor para permitir la selección por checkbox
edited_df = st.data_editor(
    df_display,
    column_config={
        "Ir a ver": st.column_config.CheckboxColumn(default=False),
        "Horario": st.column_config.TextColumn(width="small"),
        "Día": None # Ocultamos la columna día
    },
    disabled=["Horario", "Escenario", "Artista"],
    hide_index=True,
    use_container_width=True
)

# --- LÓGICA DE ITINERARIO ---
seleccionados = edited_df[edited_df["Ir a ver"] == True].sort_values("Horario")

if not seleccionados.empty:
    st.divider()
    st.header("📋 Tu Itinerario Final")
    
    # Agrupamos por horario para detectar cruces
    for horario, grupo in seleccionados.groupby("Horario"):
        with st.container():
            col1, col2 = st.columns([1, 4])
            col1.metric("Hora", horario)
            
            for _, row in grupo.iterrows():
                # Si hay más de un artista a la misma hora, mostrar alerta de cruce
                if len(grupo) > 1:
                    col2.error(f"⚠️ **CRUCE:** {row['Artista']} en el escenario {row['Escenario']}")
                else:
                    col2.success(f"✅ **{row['Artista']}** ({row['Escenario']})")
    
    st.caption("Nota: Los horarios son estimativos según la grilla oficial compartida en Instagram.")
else:
    st.info("Hacé clic en los casilleros de la tabla para armar tu cronograma.")
