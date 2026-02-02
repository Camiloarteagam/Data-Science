import streamlit as st
import pandas as pd

st.set_page_config(page_title="CR2026 Itinerario", layout="wide")

# --- DATA RESUMIDA (Basada en tus imágenes oficiales) ---
data_cr = [
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": ""},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "Ciro y Los Persas (19:40)", "Montaña": ""},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasónicos", "Sur": "La Vela Puerca (21:40)", "Montaña": "Cuarteto de Nos (20:40)"},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "Franz Ferdinand (22:40)"},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas", "Montaña": "The Chemical Brothers (00:00)"},
    # Día 2
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "Pappo x Juanse", "Montaña": "Luck Ra (16:50)"},
    {"Día": 2, "Horario": "17:50", "Norte": "Bandalos Chinos", "Sur": "El Plan de la Mariposa", "Montaña": ""},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Páez", "Sur": "Divididos (19:40)", "Montaña": "Nicki Nicole (19:40)"},
    {"Día": 2, "Horario": "21:40", "Norte": "Los Piojos", "Sur": "Trueno (21:30)", "Montaña": "Deadmau5 (22:40)"},
]

st.title("🎸 Cosquín Rock 2026: Mi Itinerario")

# 1. Filtro rápido
dia = st.sidebar.radio("Seleccioná el Día", [1, 2])
df = pd.DataFrame(data_cr)
df_dia = df[df["Día"] == dia].drop(columns=["Día"])

# 2. Visualización (La Grilla)
st.subheader("📊 Grilla de Horarios")
st.table(df_dia) # Tabla limpia para ver cruces

# 3. Selección (El "Cerebro")
st.divider()
artistas_lista = df_dia.melt(id_vars="Horario", var_name="Escenario", value_name="Artista")
artistas_lista = artistas_lista[artistas_lista["Artista"] != ""].sort_values("Horario")

# Creamos las opciones para el buscador
opciones = artistas_lista.apply(lambda x: f"{x['Horario']} - {x['Artista']} ({x['Escenario']})", axis=1).tolist()

seleccion = st.multiselect("🔍 Buscá y agregá tus bandas:", opciones)

# 4. Resultado Final
if seleccion:
    st.subheader("📋 Tu Hoja de Ruta")
    # Convertimos a tabla para que quede prolijo
    items = [s.split(" - ") for s in seleccion]
    itinerario_final = pd.DataFrame(items, columns=["Hora", "Banda"]).sort_values("Hora")
    st.success("¡Itinerario listo!")
    st.dataframe(itinerario_final, use_container_width=True, hide_index=True)
    
    # Alerta de choques
    if itinerario_final["Hora"].duplicated().any():
        st.warning("⚠️ Tenés bandas que se pisan el horario. ¡Vas a tener que elegir!")
