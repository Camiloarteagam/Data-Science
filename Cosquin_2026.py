import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="Itinerario CR2026", layout="wide")

# --- DATA COMPLETA ---
data_cr = [
    # DÍA 1
    {"Día": 1, "Horario": "14:15", "Norte": "", "Sur": "", "Montaña": "Chechi de Marcos", "Boomerang": "Microtul", "Paraguay": "", "La Casita del Blues": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Norte": "Kill Flora", "Sur": "Fantasmagoría", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "15:20", "Norte": "Eruca Sativa", "Sur": "La Mississippi", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "16:30", "Norte": "El Zar", "Sur": "Emi", "Montaña": "", "Boomerang": "Girl Ultra", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "Hermanos Gutiérrez", "Paraguay": "", "La Casita del Blues": "Perro Suizo"},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "20:40", "Norte": "", "Sur": "", "Montaña": "Cuarteto de Nos", "Boomerang": "Abel Pintos", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasónicos", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "21:40", "Norte": "", "Sur": "La Vela Puerca", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    # DÍA 2
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "", "Montaña": "Renzo Leali", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "15:10", "Norte": "", "Sur": "Kapanga", "Montaña": "", "Boomerang": "", "Paraguay": "T&K", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "Pappo x Juanse", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "17:50", "Norte": "Bándalos Chinos", "Sur": "El Plan de la Mariposa", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Páez", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "19:40", "Norte": "", "Sur": "Divididos", "Montaña": "Nicki Nicole", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "20:55", "Norte": "Airbag", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "21:30", "Norte": "", "Sur": "Trueno", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "22:40", "Norte": "", "Sur": "", "Montaña": "Deadmau5", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "23:00", "Norte": "YSY A", "Sur": "", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
    {"Día": 2, "Horario": "00:50", "Norte": "", "Sur": "Louta", "Montaña": "", "Boomerang": "", "Paraguay": "", "La Casita del Blues": ""},
]

st.title("🛡️ Matrix Simulator CR2026")
dia_sel = st.sidebar.radio("Día", [1, 2], format_func=lambda x: f"Día {x}")

# --- MATRIZ DE SELECCIÓN ---
df_full = pd.DataFrame(data_cr)
df_dia = df_full[df_full["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)
escenarios = [c for c in df_dia.columns if c != "Horario"]

# Estado de selección
if f"picks_{dia_sel}" not in st.session_state:
    st.session_state[f"picks_{dia_sel}"] = pd.DataFrame(False, index=df_dia.index, columns=escenarios)

st.subheader("1. Marcá tus artistas en la matriz")
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

# --- CONSTRUCCIÓN DEL ITINERARIO ---
itinerario_data = []
for idx, row in edited_df.iterrows():
    for esc in escenarios:
        if row[esc]:
            artista = df_dia.loc[idx, esc]
            if artista:
                itinerario_data.append({"Horario": row["Horario"], "Escenario": esc, "Artista": artista})

# --- MOSTRAR RESULTADO Y BOTÓN DESCARGA ---
if itinerario_data:
    st.divider()
    st.subheader("📋 2. Tu Itinerario (Listo para Capturar)")
    
    # Crear la matriz final de resultados
    res_df = pd.DataFrame(itinerario_data)
    matriz_final = res_df.pivot(index="Horario", columns="Escenario", values="Artista").fillna("-")
    
    # Mostrar tabla estilizada
    st.table(matriz_final)

    # Botón de "Descarga" (Instrucción manual para capturar)
    st.info("📸 **Tip:** Para llevarlo al festival, saca una captura de pantalla a la tabla de arriba. ¡Es la forma más rápida y no consume batería!")
    
    if st.button("Generar versión para compartir"):
        st.write("Aquí tienes tu selección lista:")
        st.dataframe(matriz_final, use_container_width=True)
else:
    st.info("Seleccioná casilleros en la matriz para generar tu hoja de ruta.")
