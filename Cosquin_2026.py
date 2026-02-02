import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cosquín Rock 2026 - Matrix", layout="wide")

# --- 1. DATOS UNIFICADOS DE TUS IMÁGENES ---
data_cr = [
    # DÍA 1 (Sábado 14)
    {"Día": 1, "Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "", "Blues": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "14:50", "Norte": "", "Sur": "", "Montaña": "", "Boomerang": "1915", "Blues": ""},
    {"Día": 1, "Horario": "15:00", "Norte": "", "Sur": "", "Montaña": "Ryan", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "15:50", "Norte": "", "Sur": "", "Montaña": "Bersuit Vergarabat", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "", "Boomerang": "Girl Ultra", "Blues": ""},
    {"Día": 1, "Horario": "17:10", "Norte": "", "Sur": "", "Montaña": "Marilina Bertoldi", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "18:40", "Norte": "", "Sur": "", "Montaña": "El Kuelgue", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "20:40", "Norte": "", "Sur": "", "Montaña": "Cuarteto de Nos", "Boomerang": "Abel Pintos", "Blues": ""},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasónicos", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "21:40", "Norte": "", "Sur": "La Vela Puerca", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "22:40", "Norte": "", "Sur": "", "Montaña": "Franz Ferdinand", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "00:00", "Norte": "", "Sur": "", "Montaña": "The Chemical Brothers", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas", "Montaña": "", "Boomerang": "", "Blues": ""},
    # DÍA 2 (Domingo 15)
    {"Día": 2, "Horario": "14:20", "Norte": "", "Sur": "Ainda", "Montaña": "", "Paraguay": "Wanda Jael", "Blues": ""},
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "", "Montaña": "Renzo Leali", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "15:10", "Norte": "", "Sur": "Kapanga", "Montaña": "", "Paraguay": "T&K", "Blues": ""},
    {"Día": 2, "Horario": "15:20", "Norte": "Blair", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "17:45", "Norte": "", "Sur": "El Plan de la Mariposa", "Montaña": "", "Paraguay": "", "Blues": "Cordelia's Blues"},
    {"Día": 2, "Horario": "17:50", "Norte": "Bandalos Chinos", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Páez", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "19:40", "Norte": "", "Sur": "Divididos", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "20:20", "Norte": "", "Sur": "", "Montaña": "Morat", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "20:55", "Norte": "Airbag", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "21:30", "Norte": "", "Sur": "Trueno", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "22:20", "Norte": "", "Sur": "", "Montaña": "Las Pastillas del Abuelo", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "23:00", "Norte": "YSY A", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "00:00", "Norte": "", "Sur": "", "Montaña": "Peces Raros", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "00:20", "Norte": "Caras Extrañas", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "00:50", "Norte": "", "Sur": "Louta", "Montaña": "", "Paraguay": "", "Blues": ""},
]

st.title("🛡️ Simulador Cosquín Rock 2026")
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2])

# 2. PROCESAR DATOS
df_full = pd.DataFrame(data_cr)
df_dia = df_full[df_full["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)

# 3. MATRIZ DE SELECCIÓN (Checkboxes)
# Creamos un dataframe de puros False con la misma forma que la matriz de artistas
if f"check_{dia_sel}" not in st.session_state:
    st.session_state[f"check_{dia_sel}"] = pd.DataFrame(False, index=df_dia.index, columns=df_dia.columns[1:])

st.subheader(f"Seleccioná tus bandas - Día {dia_sel}")
st.info("Hacé clic en los casilleros vacíos para elegir al artista de esa fila/columna.")

# Unimos Horario con la matriz de checkboxes para el editor
df_to_edit = pd.concat([df_dia[["Horario"]], st.session_state[f"check_{dia_sel}"]], axis=1)

edited_df = st.data_editor(
    df_to_edit,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Horario": st.column_config.TextColumn(disabled=True)
    }
)

# 4. RECONSTRUIR EL ITINERARIO
itinerario = []
# Recorremos el editor buscando dónde marcaron True
for row in range(len(edited_df)):
    hora = edited_df.iloc[row]["Horario"]
    for col in edited_df.columns[1:]: # Saltamos la columna Horario
        if edited_df.iloc[row][col] == True:
            artista = df_dia.iloc[row][col] # Buscamos el nombre real en la matriz original
            if artista != "": # Solo agregamos si hay un artista en ese horario/escenario
                itinerario.append({"Hora": hora, "Escenario": col, "Artista": artista})

# 5. MOSTRAR RESULTADOS
st.divider()
st.subheader("📋 Tu Itinerario")

if itinerario:
    final_df = pd.DataFrame(itinerario)
    st.table(final_df)
    
    # Alerta de choques
    if final_df["Hora"].duplicated().any():
        st.error("⚠️ Tenés bandas que se pisan el horario. ¡Elegí bien!")
else:
    st.write("No seleccionaste ninguna banda todavía.")
