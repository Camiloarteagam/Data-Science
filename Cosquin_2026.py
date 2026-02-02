import streamlit as st
import pandas as pd

st.set_page_config(Cosquín Rock 2026", layout="wide")

# --- DATOS OFICIALES EXTRAÍDOS DE TUS IMÁGENES ---
data_cr = [
    # DÍA 1
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
    # DÍA 2
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

st.title("🎸 Matrix Simulator: Cosquín Rock 2026")
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2])

# Filtramos y preparamos la matriz
df = pd.DataFrame(data_cr)
df_matrix = df[df["Día"] == dia_sel].drop(columns=["Día"])

st.subheader(f"Vista General - Día {dia_sel}")
st.write("Explorá los escenarios y marcá tus elegidos en la sección de itinerario.")

# Mostramos la matriz (estática para visualización clara)
st.dataframe(df_matrix, hide_index=True, use_container_width=True)

st.divider()

# Sección de Selección Interactiva
st.subheader("✅ Armá tu Itinerario")
# Para la selección, volvemos al formato de lista que es más cómodo para checkboxes en Streamlit
df_flat = df[df["Día"] == dia_sel].melt(id_vars=["Horario", "Día"], var_name="Escenario", value_name="Artista")
df_flat = df_flat[df_flat["Artista"] != ""].sort_values("Horario")

# Data editor para elegir
df_flat["Elegir"] = False
edited_selection = st.data_editor(
    df_flat[["Elegir", "Horario", "Escenario", "Artista"]],
    hide_index=True,
    use_container_width=True,
    column_config={"Elegir": st.column_config.CheckboxColumn(default=False)}
)

# Resultado final
mi_itinerario = edited_selection[edited_selection["Elegir"] == True]
if not mi_itinerario.empty:
    st.success("🔥 ¡Itinerario confirmado!")
    st.table(mi_itinerario[["Horario", "Escenario", "Artista"]])
