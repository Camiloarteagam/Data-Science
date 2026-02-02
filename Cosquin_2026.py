import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cosquín Rock 2026 - Matrix", layout="wide")

# --- DATOS EXTRAÍDOS DE TUS IMÁGENES ---
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
    {"Día": 1, "Horario": "17:50", "Norte": "Turf", "Sur": "Cruzando el Charco", "Montaña": "", "Boomerang": "Hermanos Gutiérrez", "Blues": ""},
    {"Día": 1, "Horario": "18:20", "Norte": "", "Sur": "", "Montaña": "", "Boomerang": "Indios", "Blues": ""},
    {"Día": 1, "Horario": "18:40", "Norte": "", "Sur": "", "Montaña": "El Kuelgue", "Boomerang": "", "Blues": "Misty Soul Choir"},
    {"Día": 1, "Horario": "19:20", "Norte": "", "Sur": "", "Montaña": "", "Boomerang": "Estelares", "Blues": ""},
    {"Día": 1, "Horario": "19:30", "Norte": "Dillom", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "19:40", "Norte": "", "Sur": "Ciro y Los Persas", "Montaña": "", "Boomerang": "", "Blues": ""},
    {"Día": 1, "Horario": "20:30", "Norte": "", "Sur": "", "Montaña": "", "Boomerang": "", "Blues": "Wayra Iglesias"},
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

# Preparar matriz de visualización
df = pd.DataFrame(data_cr)
df_matrix = df[df["Día"] == dia_sel].drop(columns=["Día"]).reset_index(drop=True)

# Obtener lista de artistas únicos para el selector (sin vacíos)
artistas_dia = df_matrix.melt(id_vars=["Horario"], var_name="Escenario", value_name="Artista")
artistas_dia = artistas_dia[artistas_dia["Artista"] != ""].sort_values(["Horario", "Escenario"])
artistas_opciones = artistas_dia.apply(lambda x: f"{x['Horario']} - {x['Artista']} ({x['Escenario']})", axis=1).tolist()

# --- FRONT-END ---
st.subheader(f"📅 Grilla Completa - Día {dia_sel}")
st.write("Consulta los horarios abajo y selecciona tus bandas favoritas en el panel lateral o en el buscador:")

# Mostrar matriz (Solo lectura para evitar el error de booleano)
st.dataframe(df_matrix, hide_index=True, use_container_width=True)

st.divider()

# Selección mediante multiselect (Es la forma más robusta y sin errores)
st.subheader("✅ Tu Itinerario")
seleccionados = st.multiselect(
    "Busca o selecciona los artistas que quieres ver:",
    options=artistas_opciones,
    help="Puedes escribir el nombre de la banda para encontrarla rápido."
)

if seleccionados:
    # Convertir selección en DataFrame para mostrar tabla limpia
    itinerario_data = []
    for s in seleccionados:
        hora_banda, escenario_raw = s.split(" (")
        hora, banda = hora_banda.split(" - ")
        escenario = escenario_raw.replace(")", "")
        itinerario_data.append({"Horario": hora, "Artista": banda, "Escenario": escenario})
    
    itinerario_df = pd.DataFrame(itinerario_data).sort_values("Horario")
    
    # Mostrar el itinerario
    st.success("🔥 Itinerario confirmado")
    st.table(itinerario_df)
    
    # Detectar solapamientos
    if itinerario_df["Horario"].duplicated().any():
        st.warning("⚠️ Tienes artistas seleccionados a la misma hora. ¡Vas a tener que correr!")
else:
    st.info("💡 Selecciona bandas arriba para armar tu ruta personalizada.")
