import streamlit as st
import pandas as pd

# 1. BASE DE DATOS (Se mantiene interna)
tarifas = {
    'SBO1': {'Small Van': 231100, 'NHR': 303000, 'Turbo': 350000, 'Auxiliar': 62900, 'Cap_Max': 35},
    'SAN1': {'Van': 245000, 'NHR': 303000, 'Turbo': 350000, 'Auxiliar': 62900, 'Cap_Max': 35},
    'SAV1': {'Van': 245000, 'NHR': 303000, 'Turbo': 350000, 'Auxiliar': 62900, 'Cap_Max': 35}
}

# CONFIGURACIÓN DE LA INTERFAZ
st.set_page_config(page_title="Simulador Logístico", layout="centered")
st.title("🚚 Simulador de Costos de Transporte")
st.markdown("---")

# 2. SECCIÓN DE FRONT-END (Controles)
col1, col2 = st.columns(2)

with col1:
    ciudad = st.selectbox("Selecciona la Ciudad", list(tarifas.keys()))
    vehiculo = st.selectbox("Selecciona el Vehículo", ['Small Van', 'NHR', 'Turbo'])

with col2:
    spr = st.number_input("Ingresa el SPR (Paquetes)", min_value=1, value=30)
    auxiliar = st.radio("¿Requiere Auxiliar?", ["Sí", "No"], horizontal=True)

# 3. LÓGICA DE CÁLCULO
datos = tarifas[ciudad]
costo_base = datos[vehiculo]
costo_aux = datos['Auxiliar'] if auxiliar == "Sí" else 0
total = costo_base + costo_aux
cpp = total / spr

# 4. DESPLIEGE DE RESULTADOS VISUALES
st.markdown("### Resumen de la Operación")
c1, c2, c3 = st.columns(3)
c1.metric("Costo Total", f"${total:,}")
c2.metric("Costo por Paquete", f"${cpp:,.2f}")
c3.metric("Ocupación", f"{(spr/datos['Cap_Max'])*100:.1f}%")

# Alerta visual si se supera la capacidad
if spr > datos['Cap_Max']:
    st.error(f"⚠️ El SPR de {spr} supera la capacidad máxima de la {vehiculo} ({datos['Cap_Max']})")

# Tabla de sensibilidad interactiva
with st.expander("Ver análisis de rentabilidad (Variación de SPR)"):
    tabla = []
    for s in [spr-5, spr, spr+5, spr+10]:
        if s > 0:
            tabla.append({"Paquetes": s, "Costo Unitario": f"${total/s:,.0f}"})
    st.table(pd.DataFrame(tabla))
