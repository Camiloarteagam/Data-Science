import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simulador Cosquín Rock 2026", layout="wide")

# --- BASE DE DATOS COMPLETA SEGÚN TUS IMÁGENES ---
data_cr = [
    # DÍA 1 - SÁBADO 14 (Basado en)
    {"Día": 1, "Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "Microtul", "Paraguay": "", "La Casita del Blues": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "14:50", "Norte": "", "Sur": "", "Montaña": "", "Boomerang": "1915", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "15:50", "Norte": "", "Sur": "", "Montaña": "Bersuit Vergarabat", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "", "Boomerang": "Girl Ultra", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "17:10", "Norte": "", "Sur": "", "Montaña": "Marilina Bertoldi", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "Hermanos Gutiérrez", "Paraguay": "", "La Casita del Blues": "Perro Suizo"},
    {"Día": 1, "Horario": "18:40", "Norte": "", "Sur": "", "Montaña": "El Kuelgue", "Boomerang": "", "Paraguay": "", "La Casita del Blues": "Misty Soul Choir"},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "20:40", "Norte": "", "Sur": "", "Montaña": "Cuarteto de Nos", "Boomerang": "Abel Pintos", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasónicos", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "21:40", "Norte": "", "Sur": "La Vela Puerca", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "22:40", "Norte": "", "Sur": "", "Montaña": "Franz Ferdinand", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "", "Boomerang": "Coti", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "00:00", "Norte": "", "Sur": "", "Montaña": "The Chemical Brothers", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas x Fachi y Abel", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},

    # DÍA 2 - DOMINGO 15 (Basado en)
    {"Día": 2, "Horario": "14:20", "Norte": "", "Sur": "Ainda", "Montaña": "", "Boomerang": "", "Paraguay": "Wanda Jael", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "", "Montaña": "Renzo Leali", "Boomerang": "", "Paraguay": "", "La Casita del Blues": "Rosy Gomeez"},
    {"Día": 2, "Horario": "15:10", "Norte": "", "Sur": "Kapanga", "Montaña": "", "Boomerang": "", "Paraguay": "T&K", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "15:20", "Norte": "Blair", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "15:50", "Norte": "", "Sur": "", "Montaña": "Gustavo Cordera", "Boomerang": "", "Paraguay": "", "La Casita del Blues": "Rudy"},
    {"Día": 2, "Horario": "16:25", "Norte": "", "Sur": "Pappo x Juanse", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "16:50", "Norte": "", "Sur": "", "Montaña": "Luck Ra", "Boomerang": "", "Paraguay": "", "La Casita del Blues": "Bulldozer Blues Band"},
    {"Día": 2, "Horario": "17:00", "Norte": "", "Sur": "", "Montaña": "Los Pericos", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "17:45", "Norte": "", "Sur": "El Plan de la Mariposa", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": "Cordelia's Blues"},
    {"Día": 2, "Horario": "17:50", "Norte": "Bándalos Chinos", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "18:20", "Norte": "", "Sur": "", "Montaña": "Usted Señalemelo", "Boomerang": "", "Paraguay": "Devendra Banhart", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Páez", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "19:40", "Norte": "", "Sur": "Divididos", "Montaña": "Nicki Nicole", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "20:20", "Norte": "", "Sur": "", "Montaña": "Morat", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "20:30", "Norte": "", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "Marky Ramone", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "20:55", "Norte": "Airbag", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "21:30", "Norte": "", "Sur": "Trueno", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "22:20", "Norte": "", "Sur": "", "Montaña": "Las Pastillas del Abuelo", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "22:40", "Norte": "", "Sur": "", "Montaña": "Deadmau5", "Boomerang": "", "Paraguay": "", "La Casita del Blues": "Xime Monzón"},
    {"Día": 2, "Horario": "23:00", "Norte": "YSY A", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "00:00", "Norte": "", "Sur": "", "Montaña": "Peces Raros", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "00:20", "Norte": "Caras Extrañas", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "00:50", "Norte": "", "Sur": "Louta", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
]

st.title("🎸 Matrix Simulator: Cosquín Rock 2026")
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2], format_func=lambda x: f"Día {x}")

# --- PROCESAMIENTO DE MATRIZ ---
df_full = pd.DataFrame(data_cr)
df_dia = df_full[df_full["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)
escenarios = [c for c in df_dia.columns if c != "Horario"]

# Matriz Espejo de Selección (Booleanos)
if f"picks_{dia_sel}" not in st.session_state:
    st.session_state[f"picks_{dia_sel}"] = pd.DataFrame(False, index=df_dia.index, columns=escenarios)

st.subheader("1. Consultá la Grilla y seleccioná los casilleros abajo")
st.dataframe(df_dia, hide_index=True, use_container_width=True)

st.divider()

st.subheader("✅ 2. Matriz de Selección (Marcá el cuadrito correspondiente)")
# Mezclamos el horario con los checkboxes
selector_df = pd.concat([df_dia[["Horario"]], st.session_state[f"picks_{dia_sel}"]], axis=1)

edited_df = st.data_editor(
    selector_df,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Horario": st.column_config.TextColumn(disabled=True),
        **{esc: st.column_config.CheckboxColumn(label=esc) for esc in escenarios}
    }
)

# --- RESULTADO DEL ITINERARIO ---
itinerario = []
for idx, row in edited_df.iterrows():
    hora = row["Horario"]
    for esc in escenarios:
        if row[esc]:
            artista_nombre = df_dia.loc[idx, esc]
            if artista_nombre:
                itinerario.append({"Horario": hora, "Escenario": esc, "Artista": artista_nombre})

st.divider()
st.subheader("📋 Tu Itinerario Final")

if itinerario:
    final_df = pd.DataFrame(itinerario).sort_values("Horario")
    st.table(final_df)
    
    if final_df["Horario"].duplicated().any():
        st.error("⚠️ Tienes artistas seleccionados a la misma hora.")
else:
    st.info("Marcá los casilleros en la matriz para armar tu ruta.")
