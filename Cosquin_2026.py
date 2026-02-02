import streamlit as st
import pandas as pd

st.set_page_config(page_title="Matrix Cosquín Rock 2026", layout="wide")

# --- BASE DE DATOS EXTRAÍDA DE LAS IMÁGENES ---
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
    {"Día": 1, "Horario": "18:40", "Norte": "", "Sur": "", "Montaña": "El Kuelgue", "Boomerang": "", "Blues": "Misty Soul Choir"},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "20:40", "Norte": "", "Sur": "", "Montaña": "Cuarteto de Nos", "Boomerang": "Abel Pintos", "Blues": ""},
    {"Día": 1, "Horario": "21:20", "Norte": "Babasonicos", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "21:40", "Norte": "", "Sur": "La Vela Puerca", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "22:40", "Norte": "", "Sur": "", "Montaña": "Franz Ferdinand", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "23:20", "Norte": "Lali", "Sur": "Las Pelotas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "00:00", "Norte": "", "Sur": "", "Montaña": "The Chemical Brothers", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "00:40", "Norte": "Caligaris", "Sur": "Viejas Locas x Fachi y Abel", "Montaña": "", "Boomerang": "", "Blues": ""},
    # DÍA 2
    {"Día": 2, "Horario": "14:20", "Norte": "", "Sur": "Ainda", "Montaña": "", "Paraguay": "Wanda Jael", "Blues": ""},
    {"Día": 2, "Horario": "14:30", "Norte": "Sofi Mora", "Sur": "", "Montaña": "Renzo Leali", "Paraguay": "", "Blues": "Rosy Gomeez"},
    {"Día": 2, "Horario": "15:10", "Norte": "", "Sur": "Kapanga", "Montaña": "", "Paraguay": "T&K", "Blues": ""},
    {"Día": 2, "Horario": "15:20", "Norte": "Blair", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "16:25", "Norte": "", "Sur": "Pappo x Juanse", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "16:30", "Norte": "Gauchito Club", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "17:45", "Norte": "", "Sur": "El Plan de la Mariposa", "Montaña": "", "Paraguay": "", "Blues": "Cordelia's Blues"},
    {"Día": 2, "Horario": "17:50", "Norte": "Bandalos Chinos", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "18:20", "Norte": "", "Sur": "", "Montaña": "", "Paraguay": "Devendra Banhart", "Blues": ""},
    {"Día": 2, "Horario": "18:30", "Norte": "", "Sur": "", "Montaña": "Silvestre y La Naranja", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "19:10", "Norte": "Fito Paez", "Sur": "", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "19:40", "Norte": "", "Sur": "Divididos", "Montaña": "", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "20:20", "Norte": "", "Sur": "", "Montaña": "Morat", "Paraguay": "", "Blues": ""},
    {"Día": 2, "Horario": "20:30", "Norte": "", "Sur": "", "Montaña": "", "Paraguay": "Marky Ramone", "Blues": ""},
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

# Preparar matriz
df = pd.DataFrame(data_cr)
df_matrix = df[df["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)

# Crear lista de artistas para el selector
artistas_dia = df_matrix.melt(id_vars=["Horario"], var_name="Escenario", value_name="Artista")
artistas_dia = artistas_dia[artistas_dia["Artista"] != ""].sort_values(["Horario", "Escenario"])
opciones = artistas_dia.apply(lambda x: f"{x['Horario']} - {x['Artista']} ({x['Escenario']})", axis=1).tolist()

# --- FRONT-END ---
st.subheader(f"📅 Grilla Completa - Día {dia_sel}")
# Mostrar matriz de solo lectura para evitar errores de interpretación booleanos
st.dataframe(df_matrix, hide_index=True, use_container_width=True)

st.divider()

# Selector que sí guarda la información correctamente
st.subheader("✅ Seleccioná tus bandas")
seleccionados = st.multiselect(
    "Busca y elige los artistas para armar tu ruta:",
    options=opciones
)

if seleccionados:
    itinerario = []
    for s in seleccionados:
        hora_banda, esc_raw = s.split(" (")
        hora, banda = hora_banda.split(" - ")
        esc = esc_raw.replace(")", "")
        itinerario.append({"Horario": hora, "Artista": banda, "Escenario": esc})
    
    itinerario_df = pd.DataFrame(itinerario).sort_values("Horario")
    st.success("🔥 Itinerario confirmado")
    st.table(itinerario_df)
    
    # Aviso de solapamientos
    if itinerario_df["Horario"].duplicated().any():
        st.warning("⚠️ ¡Atención! Tienes bandas seleccionadas al mismo horario.")
else:
    st.info("💡 Usa el selector de arriba para agregar artistas a tu itinerario.")
