import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simulador Cosquín Rock 2026", layout="wide")

# --- BASE DE DATOS BASADA EN LAS IMÁGENES OFICIALES ---
data_cr = [
    # DÍA 1 (Sábado 14)
    {"Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "", "Blues": "Golo's Band"},
    {"Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "", "Boomerang": "Girl Ultra", "Blues": ""},
    {"Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Horario": "20:40", "Norte": "", "Sur": "", "Montaña": "Cuarteto de Nos", "Boomerang": "Abel Pintos", "Blues": ""},
    {"Horario": "21:20", "Norte": "Babasónicos", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Horario": "21:40", "Norte": "", "Sur": "La Vela Puerca", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Horario": "22:40", "Norte": "", "Sur": "", "Montaña": "Franz Ferdinand", "Boomerang": "", "Blues": ""},
    {"Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Horario": "00:00", "Norte": "", "Sur": "", "Montaña": "The Chemical Brothers", "Boomerang": "", "Blues": ""},
    {"Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas", "Montaña": "", "Boomerang": "", "Blues": ""},
]

st.title("🎸 Simulador de Itinerario: Cosquín Rock 2026")
st.markdown("### Selecciona tus artistas directamente en la grilla")
st.info("💡 **Instrucciones:** Haz doble clic o presiona 'Espacio' sobre el nombre de un artista para marcarlo/desmarcarlo.")

# Creamos la matriz de nombres
df_original = pd.DataFrame(data_cr)
escenarios = ["Norte", "Sur", "Montaña", "Boomerang", "Blues"]

# Inicializamos el estado de selección en la sesión si no existe
if "seleccionados" not in st.session_state:
    st.session_state.seleccionados = set()

# Función para formatear el texto de la celda (Nombre + Check visual)
def format_cell(artista, horario, escenario):
    if not artista:
        return ""
    key = f"{horario}|{escenario}|{artista}"
    icon = "✅ SELECCIONADO" if key in st.session_state.seleccionados else "⬜ (Click para elegir)"
    return f"{artista}\n{icon}"

# Creamos el DataFrame que se mostrará en el editor
df_display = df_original.copy()
for esc in escenarios:
    df_display[esc] = df_display.apply(lambda x: format_cell(x[esc], x["Horario"], esc), axis=1)

# --- EDITOR DE DATOS INTERACTIVO ---
edited_df = st.data_editor(
    df_display,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Horario": st.column_config.TextColumn(disabled=True),
        **{esc: st.column_config.TextColumn(width="medium") for esc in escenarios}
    },
    key="editor_grilla"
)

# Lógica para actualizar la selección basándose en los cambios del editor
# (Se detecta qué celda fue "editada" por el usuario)
if st.session_state.editor_grilla:
    edits = st.session_state.editor_grilla.get("edited_rows", {})
    for row_idx, changes in edits.items():
        for esc, val in changes.items():
            horario = df_original.iloc[row_idx]["Horario"]
            artista = df_original.iloc[row_idx][esc]
            if artista:
                key = f"{horario}|{esc}|{artista}"
                if key in st.session_state.seleccionados:
                    st.session_state.seleccionados.remove(key)
                else:
                    st.session_state.seleccionados.add(key)
    st.rerun()

# --- MOSTRAR EL ITINERARIO FINAL ---
st.divider()
st.subheader("📋 Tu Hoja de Ruta")

if st.session_state.seleccionados:
    itinerario = []
    for item in st.session_state.seleccionados:
        h, e, a = item.split("|")
        itinerario.append({"Hora": h, "Escenario": e, "Artista": a})
    
    final_df = pd.DataFrame(itinerario).sort_values("Hora")
    st.table(final_df)
    
    # Alerta de choques horarias
    if final_df["Hora"].duplicated().any():
        st.error("⚠️ Tienes artistas que se pisan el horario. Revisa los escenarios Norte, Sur y Montaña.")
else:
    st.write("Aún no has seleccionado ningún artista.")
