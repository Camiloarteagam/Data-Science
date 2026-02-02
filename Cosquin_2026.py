import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simulador Cosquín Rock 2026", layout="wide")

# --- BASE DE DATOS COMPLETA (Día 1 y 2) ---
data_cr = [
    # DÍA 1
    {"Día": 1, "Horario": "14:15", "Escenario": "Montaña", "Artista": "Chechi de Marcos"},
    {"Día": 1, "Horario": "14:15", "Escenario": "La Casita del Blues", "Artista": "Golo's Band"},
    {"Día": 1, "Horario": "14:30", "Escenario": "Norte", "Artista": "Kill Flora"},
    {"Día": 1, "Horario": "14:30", "Escenario": "Sur", "Artista": "Fantasmagoría"},
    {"Día": 1, "Horario": "14:50", "Escenario": "Boomerang", "Artista": "1915"},
    {"Día": 1, "Horario": "15:20", "Escenario": "Norte", "Artista": "Eruca Sativa"},
    {"Día": 1, "Horario": "15:20", "Escenario": "Sur", "Artista": "La Mississippi"},
    {"Día": 1, "Horario": "16:30", "Escenario": "Norte", "Artista": "El Zar"},
    {"Día": 1, "Horario": "16:30", "Escenario": "Sur", "Artista": "Emi"},
    {"Día": 1, "Horario": "16:30", "Escenario": "Boomerang", "Artista": "Girl Ultra"},
    {"Día": 1, "Horario": "17:50", "Escenario": "Norte", "Artista": "Turf"},
    {"Día": 1, "Horario": "17:50", "Escenario": "Sur", "Artista": "Cruzando el Charco"},
    {"Día": 1, "Horario": "19:30", "Escenario": "Norte", "Artista": "Dillom"},
    {"Día": 1, "Horario": "19:40", "Escenario": "Sur", "Artista": "Ciro y Los Persas"},
    {"Día": 1, "Horario": "20:40", "Escenario": "Montaña", "Artista": "Cuarteto de Nos"},
    {"Día": 1, "Horario": "20:40", "Escenario": "Boomerang", "Artista": "Abel Pintos"},
    {"Día": 1, "Horario": "21:20", "Escenario": "Norte", "Artista": "Babasónicos"},
    {"Día": 1, "Horario": "21:40", "Escenario": "Sur", "Artista": "La Vela Puerca"},
    {"Día": 1, "Horario": "23:20", "Escenario": "Norte", "Artista": "Lali"},
    {"Día": 1, "Horario": "23:20", "Escenario": "Sur", "Artista": "Las Pelotas"},
    {"Día": 1, "Horario": "00:00", "Escenario": "Montaña", "Artista": "The Chemical Brothers"},
    {"Día": 1, "Horario": "00:40", "Escenario": "Norte", "Artista": "Caligaris"},
    {"Día": 1, "Horario": "00:40", "Escenario": "Sur", "Artista": "Viejas Locas x Fachi y Abel"},
    # DÍA 2
    {"Día": 2, "Horario": "14:30", "Escenario": "Norte", "Artista": "Sofi Mora"},
    {"Día": 2, "Horario": "15:10", "Escenario": "Sur", "Artista": "Kapanga"},
    {"Día": 2, "Horario": "15:10", "Escenario": "Paraguay", "Artista": "T&K"},
    {"Día": 2, "Horario": "16:30", "Escenario": "Norte", "Artista": "Gauchito Club"},
    {"Día": 2, "Horario": "17:50", "Escenario": "Norte", "Artista": "Bándalos Chinos"},
    {"Día": 2, "Horario": "19:10", "Escenario": "Norte", "Artista": "Fito Páez"},
    {"Día": 2, "Horario": "19:40", "Escenario": "Sur", "Artista": "Divididos"},
    {"Día": 2, "Horario": "19:40", "Escenario": "Montaña", "Artista": "Nicki Nicole"},
    {"Día": 2, "Horario": "20:55", "Escenario": "Norte", "Artista": "Airbag"},
    {"Día": 2, "Horario": "21:30", "Escenario": "Sur", "Artista": "Trueno"},
    {"Día": 2, "Horario": "22:40", "Escenario": "Montaña", "Artista": "Deadmau5"},
    {"Día": 2, "Horario": "23:00", "Escenario": "Norte", "Artista": "YSY A"},
    {"Día": 2, "Horario": "00:50", "Escenario": "Sur", "Artista": "Louta"},
]

st.title("🎸 Matrix Simulator: Cosquín Rock 2026")

# 1. Selección de Día y Artistas (Lista Desplegable)
dia_sel = st.sidebar.radio("Seleccioná el día", [1, 2], format_func=lambda x: f"Día {x}")

df = pd.DataFrame(data_cr)
df_dia = df[df["Día"] == dia_sel].sort_values("Horario")

# Generamos las opciones para la lista desplegable
opciones = df_dia.apply(lambda x: f"{x['Horario']} - {x['Artista']} ({x['Escenario']})", axis=1).tolist()

st.subheader("✅ 1. Seleccioná tus artistas favoritos")
seleccion = st.multiselect(
    "Escribí o buscá las bandas que querés ver:",
    options=opciones,
    placeholder="Ej: La Vela Puerca, Babasónicos..."
)

# 2. Procesamiento del Resultado
if seleccion:
    st.divider()
    st.subheader("📋 2. Tu Itinerario en Formato Matriz")
    
    # Extraemos los datos de la selección
    data_itinerario = []
    for s in seleccion:
        hora_banda, esc_raw = s.split(" (")
        hora, banda = hora_banda.split(" - ")
        esc = esc_raw.replace(")", "")
        data_itinerario.append({"Horario": hora, "Escenario": esc, "Artista": banda})
    
    # Creamos un DataFrame con los seleccionados
    res_df = pd.DataFrame(data_itinerario)
    
    # Pivotamos para crear la matriz: Horario en Filas, Escenario en Columnas
    try:
        matriz_final = res_df.pivot(index="Horario", columns="Escenario", values="Artista").fillna("")
        
        # Reordenar columnas para que siempre sigan un orden lógico
        orden_escenarios = ["Norte", "Sur", "Montaña", "Boomerang", "Paraguay", "La Casita del Blues"]
        columnas_presentes = [esc for esc in orden_escenarios if esc in matriz_final.columns]
        matriz_final = matriz_final[columnas_presentes]
        
        # Mostrar la matriz resultante
        st.table(matriz_final)
        
        # Alerta de choques horaria
        if res_df["Horario"].duplicated().any():
            st.warning("⚠️ ¡Atención! Tenés artistas que se pisan el horario en diferentes escenarios.")
            
    except Exception as e:
        st.error("Hubo un error al generar la matriz. Asegurate de no haber seleccionado al mismo artista dos veces.")
else:
    st.info("💡 Usá la lista desplegable arriba para empezar a armar tu ruta.")
