import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

# Título y textos
st.title("🔍 Mi Aplicación Streamlit Completa")
st.header("1. Encabezados")
st.subheader("1.1. Subencabezado")
st.text("1.2. Texto plano de ejemplo")
st.markdown(
    """
1.3. Markdown con formato:

- **Negrita**
- _Itálica_
- [Enlace](https://streamlit.io)
"""
)
st.caption("1.4. Pie de foto o ayuda")
st.latex(r"E = mc^2")

# Imágenes, audio y video
st.header("2. Multimedia")
st.image("static/image/polo.jpg", caption="2.1. Imagen de ejemplo")
st.audio("static/audio/night-detective-226857.mp3", format="audio/mp3")
st.video("static/video/test.mp4", format="video/mp4")

# Widgets de interacción
st.header("3. Widgets básicos")
if st.button("3.1. Presiona este botón"):
    st.write("¡Botón presionado!")

chk = st.checkbox("3.2. Marcar opción")
if chk:
    st.write("Checkbox marcado")

sel = st.selectbox("3.3. Selecciona una opción", ["Opción A", "Opción B", "Opción C"])
st.write("Seleccionaste:", sel)

multi = st.multiselect("3.4. Selección múltiple", ["🐱 Gato", "🐶 Perro", "🐰 Conejo"])
st.write("Animales elegidos:", multi)

st.slider("3.5. Slider (0–100)", 0, 100, 25)
st.radio("3.6. Radio buttons", ["Rojo", "Verde", "Azul"], index=2)

st.date_input("3.7. Fecha de hoy", datetime.now().date())
st.time_input("3.8. Hora actual", datetime.now().time())

# Carga de archivos
st.header("4. Carga de archivos")
archivo = st.file_uploader("4.1. Sube un CSV", type="csv")
if archivo is not None:
    df = pd.read_csv(archivo)
    st.dataframe(df)

# Cámara y selector de color
st.header("5. Cámara y color")
foto = st.camera_input("5.1. Toma una foto")
if foto:
    st.image(foto)

color = st.color_picker("5.2. Elige un color", "#00f900")
st.write("Color elegido:", color)

# Layout: columnas, expander y tabs
st.header("6. Layout avanzado")
col1, col2 = st.columns(2)
with col1:
    st.metric("6.1. Temperatura", "25 °C", delta="+1.2 °C")
with col2:
    st.metric("6.2. Humedad", "60 %", delta="-5 %")

with st.expander("6.3. Más detalles"):
    st.write("Contenido oculto dentro de un expander.")

tab1, tab2 = st.tabs(["Tabla aleatoria", "Gráfica"])
with tab1:
    df2 = pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE"))
    st.table(df2)
with tab2:
    st.line_chart(df2)

# Mapas
st.header("7. Mapas")
df_map = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [19.43, -99.13],
    columns=["lat", "lon"],
)
st.map(df_map)

# Formulario
st.header("8. Formularios")
with st.form("mi_formulario"):
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", 0, 120, 30)
    enviado = st.form_submit_button("Enviar")
if enviado:
    st.success(f"Bienvenido {nombre}, tienes {edad} años")

# Sidebar
st.sidebar.header("9. Barra Lateral")
op = st.sidebar.radio("Navegación", ["Inicio", "Configuración"])
st.sidebar.write("Selección:", op)

# Progreso y feedback
st.header("10. Indicadores de Progreso")
with st.spinner("Procesando..."):
    time.sleep(1)
st.success("¡Proceso completado!")

progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.005)

# Caching
@st.cache
def cargar_datos(n):
    return np.random.randn(n, 3)

data_cached = cargar_datos(50_000)
st.write("Datos cacheados (primeros 5 registros):", data_cached[:5])

# Efecto visual final
st.balloons()