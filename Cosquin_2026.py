import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simulador Cosquín Rock 2026", layout="wide")

# --- BASE DE DATOS (Día 1 y 2 extraídos de tus imágenes) ---
data_cr = [
    # DÍA 1
    {"Día": 1, "Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "Microtul", "Blues": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "14:50", "Norte": "", "Sur": "", "Montaña": "", "Boomerang": "1915", "Blues": ""},
    {"Día": 1, "Horario": "15:00", "Norte": "", "Sur": "", "Montaña": "Ryan", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "15:50", "Norte": "", "Sur": "", "Montaña": "Bersuit Vergarabat", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "", "Boomerang": "Girl Ultra", "Blues": ""},
    {"Día": 1, "Horario": "17:10", "Norte": "", "Sur": "", "Montaña": "Marilina Bertoldi", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "18:40", "Norte": "", "Sur": "", "Montaña": "El Kuelgue", "Boomerang": "", "Blues": "Misty Soul Choir"},
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
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "", "Montaña": "Renzo Leali", "Paraguay": "", "Blues": "Rosy Gomeez"},
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

st.title("🎸 Matrix Selector - Cosquín Rock 2026")
dia_sel = st.sidebar.radio("Día", [1, 2], format_func=lambda x: f"Día {x}")

# --- PROCESAMIENTO ---
df_full = pd.DataFrame(data_cr)
df_dia = df_full[df_full["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)

# --- VISTA 1: REFERENCIA (NO EDITABLE) ---
st.subheader("📖 1. Consulta la Grilla")
st.dataframe(df_dia, use_container_width=True, hide_index=True)

st.divider()

# --- VISTA 2: SELECCIÓN (MATRIZ DE CHECKBOXES) ---
st.subheader("✅ 2. Marca tus Elegidos")
st.info("Marca el casillero correspondiente a la celda del artista que quieres ver arriba.")

# Creamos la matriz de checkboxes alineada con los datos
escenarios = [c for c in df_dia.columns if c != "Horario"]
if f"picks_{dia_sel}" not in st.session_state:
    st.session_state[f"picks_{dia_sel}"] = pd.DataFrame(False, index=df_dia.index, columns=escenarios)

# Editor de la matriz de selección
select_df = pd.concat([df_dia[["Horario"]], st.session_state[f"picks_{dia_sel}"]], axis=1)
edited_df = st.data_editor(
    select_df,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Horario": st.column_config.TextColumn(disabled=True),
        **{esc: st.column_config.CheckboxColumn() for esc in escenarios}
    }
)

# --- RESULTADO FINAL ---
itinerario = []
for idx, row in edited_df.iterrows():
    hora = row["Horario"]
    for esc in escenarios:
        if row[esc] == True:
            artista = df_dia.loc[idx, esc]
            if artista: # Solo agregar si hay un nombre en esa celda
                itinerario.append({"Hora": hora, "Escenario": esc, "Artista": artista})

st.divider()
st.subheader("📝 3. Tu Itinerario Generado")

if itinerario:
    res_df = pd.DataFrame(itinerario).sort_values("Hora")
    st.table(res_df)
    
    # Detección de colisiones
    if res_df["Hora"].duplicated().any():
        st.warning("⚠️ ¡Atención! Tienes bandas seleccionadas al mismo horario.")
else:
    st.write("Selecciona casilleros en la matriz para ver tu plan aquí.")
