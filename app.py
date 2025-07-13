import streamlit as st
import pandas as pd

st.title("📊 Análisis de Datos con Streamlit")

# Subir archivo CSV
archivo = st.file_uploader("Carga tu archivo CSV", type=["csv"])

if archivo:
    df = pd.read_csv(archivo)
    st.subheader("📄 Vista previa de los datos")
    st.dataframe(df)

    st.subheader("🔍 Estadísticas Descriptivas")
    st.write(df.describe())

    st.subheader("📈 Selección de columna para histograma")
    columna = st.selectbox("Selecciona una columna numérica", df.select_dtypes(include="number").columns)
    if columna:
        st.bar_chart(df[columna].value_counts())
else:
    st.info("Por favor, carga un archivo CSV para comenzar.")

# Personalización adicional
st.sidebar.title("Configuraciones")
modo_oscuro = st.sidebar.checkbox("Activar modo oscuro")
if modo_oscuro:
    st.write("🌙 El modo oscuro está activado… aunque aún no cambia la interfaz 😅")

st.markdown("---")
st.caption("Este ejemplo demuestra carga de datos, vista previa, estadísticas y gráficos interactivos.")