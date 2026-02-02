import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuración de la interfaz
st.set_page_config(page_title="Simulador Cosquín Rock 2026", page_icon="🎸", layout="centered")

# --- BASE DE DATOS OFICIAL (Basada en tus imágenes) ---
data = [
    # DÍA 1 - SÁBADO 14
    {"dia": 1, "escenario": "Norte", "artista": "Kill Flora", "inicio": "14:30"},
    {"dia": 1, "escenario": "Norte", "artista": "Eruca Sativa", "inicio": "15:20"},
    {"dia": 1, "escenario": "Norte", "artista": "El Zar", "inicio": "16:30"},
    {"dia": 1, "escenario": "Norte", "artista": "Turf", "inicio": "17:50"},
    {"dia": 1, "escenario": "Norte", "artista": "Dillom", "inicio": "19:30"},
    {"dia": 1, "escenario": "Norte", "artista": "Babasónicos", "inicio": "21:20"},
    {"dia": 1, "escenario": "Norte", "artista": "Lali", "inicio": "23:20"},
    {"dia": 1, "escenario": "Norte", "artista": "Caligaris", "inicio": "00:40"},
    
    {"dia": 1, "escenario": "Sur", "artista": "Fantasmagoría", "inicio": "14:30"},
    {"dia": 1, "escenario": "Sur", "artista": "La Mississippi", "inicio": "15:20"},
    {"dia": 1, "escenario": "Sur", "artista": "Emi", "inicio": "16:30"},
    {"dia": 1, "escenario": "Sur", "artista": "Cruzando el Charco", "inicio": "17:50"},
    {"dia": 1, "escenario": "Sur", "artista": "Ciro y Los Persas", "inicio": "19:40"},
    {"dia": 1, "escenario": "Sur", "artista": "La Vela Puerca", "inicio": "21:40"},
    {"dia": 1, "escenario": "Sur", "artista": "Las Pelotas", "inicio": "23:20"},
    {"dia": 1, "escenario": "Sur", "artista": "Viejas Locas x Fachi y Abel", "inicio": "00:40"},
    
    {"dia": 1, "escenario": "Montaña", "artista": "Chechi de Marcos", "inicio": "14:15"},
    {"dia": 1, "escenario": "Montaña", "artista": "Ryan", "inicio": "15:00"},
    {"dia": 1, "escenario": "Montaña", "artista": "Bersuit Vergarabat", "inicio": "15:50"},
    {"dia": 1, "escenario": "Montaña", "artista": "Marilina Bertoldi", "inicio": "17:10"},
    {"dia": 1, "escenario": "Montaña", "artista": "El Kuelgue", "inicio": "18:40"},
    {"dia": 1, "escenario": "Montaña", "artista": "Cuarteto de Nos", "inicio": "20:40"},
    {"dia": 1, "escenario": "Montaña", "artista": "Franz Ferdinand", "inicio": "22:40"},
    {"dia": 1, "escenario": "Montaña", "artista": "The Chemical Brothers (DJ Set)", "inicio": "00:00"},
    
    # DÍA 2 - DOMINGO 15
    {"dia": 2, "escenario": "Norte", "artista": "Sofi Mora", "inicio": "14:30"},
    {"dia": 2, "escenario": "Norte", "artista": "Blair", "inicio": "15:20"},
    {"dia": 2, "escenario": "Norte", "artista": "Gauchito Club", "inicio": "16:30"},
    {"dia": 2, "escenario": "Norte", "artista": "Bandalos Chinos", "inicio": "17:50"},
    {"dia": 2, "escenario": "Norte", "artista": "Fito Páez", "inicio": "19:10"},
    {"dia": 2, "escenario": "Norte", "artista": "Airbag", "inicio": "20:55"},
    {"dia": 2, "escenario": "Norte", "artista": "YSY A", "inicio": "23:00"},
    {"dia": 2, "escenario": "Norte", "artista": "Caras Extrañas", "inicio": "00:20"},
    
    {"dia": 2, "escenario": "Sur", "artista": "Ainda", "inicio": "14:20"},
    {"dia": 2, "escenario": "Sur", "artista": "Kapanga", "inicio": "15:10"},
    {"dia": 2, "escenario": "Sur", "artista": "Pappo x Juanse", "inicio": "16:25"},
    {"dia": 2, "escenario": "Sur", "artista": "El Plan de la Mariposa", "inicio": "17:45"},
    {"dia": 2, "escenario": "Sur", "artista": "Divididos", "inicio": "19:40"},
    {"dia": 2, "escenario": "Sur", "artista": "Trueno", "inicio": "21:30"},
    {"dia": 2, "escenario": "Sur", "artista": "Guasones", "inicio": "23:10"},
    {"dia": 2, "escenario": "Sur", "artista": "Louta", "inicio": "00:50"},

    {"dia": 2, "escenario": "Montaña", "artista": "Renzo Leali", "inicio": "14:30"},
    {"dia": 2, "escenario": "Montaña", "artista": "Beats Modernos", "inicio": "15:00"},
    {"dia": 2, "escenario": "Montaña", "artista": "Gustavo Cordera", "inicio": "15:50"},
    {"dia": 2, "escenario": "Montaña", "artista": "Los Pericos", "inicio": "17:00"},
    {"dia": 2, "escenario": "Montaña", "artista": "Silvestre y La Naranja", "inicio": "18:30"},
    {"dia": 2, "escenario": "Montaña", "artista": "Morat", "inicio": "20:20"},
    {"dia": 2, "escenario": "Montaña", "artista": "Las Pastillas del Abuelo", "inicio": "22:20"},
    {"dia": 2, "escenario": "Montaña", "artista": "Peces Raros", "inicio": "00:00"},
    {"dia": 2, "escenario": "Montaña", "artista": "Mariano Mellino", "inicio": "01:00"},
]

# --- LÓGICA DE LA APP ---
st.title("🎸 Cosquín Rock 2026 - Simulador")
st.markdown("Crea tu itinerario y detecta si se te pisan las bandas.")

dia = st.sidebar.radio("Selecciona el día:", [1, 2], format_func=lambda x: f"Día {x} (Sábado)" if x==1 else f"Día {x} (Domingo)")

# Filtrar datos por día
df = pd.DataFrame(data)
df_dia = df[df['dia'] == dia].sort_values(by="inicio")

# Multiselect de artistas
opciones = df_dia.apply(lambda x: f"{x['inicio']} - {x['artista']} [{x['escenario']}]", axis=1).tolist()
seleccion = st.multiselect("Elige los shows que quieres ver:", opciones)

if seleccion:
    st.subheader("📅 Tu Itinerario")
    
    # Procesar selección para detectar choques
    itinerario = []
    for item in seleccion:
        hora_str = item.split(" - ")[0]
        nombre = item.split(" - ")[1]
        itinerario.append({"hora": hora_str, "info": nombre})
    
    # Ordenar por hora
    itinerario.sort(key=lambda x: x['hora'])

    # Mostrar con advertencias si hay colisión
    for i in range(len(itinerario)):
        col1, col2 = st.columns([1, 4])
        col1.write(f"**{itinerario[i]['hora']}**")
        
        # Si la hora es igual a la anterior, mostrar alerta
        if i > 0 and itinerario[i]['hora'] == itinerario[i-1]['hora']:
            col2.error(f"⚠️ CONFLICTO: {itinerario[i]['info']}")
        else:
            col2.success(itinerario[i]['info'])

    st.info("💡 Consejo: Recuerda que caminar entre escenarios Norte y Sur puede llevarte hasta 15 minutos.")
else:
    st.warning("Selecciona al menos un artista para empezar.")

st.sidebar.markdown("---")
st.sidebar.write("Desarrollado para el Cosquín Rock 2026")
