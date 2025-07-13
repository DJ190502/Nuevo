import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Título de la aplicación
st.title("Aplicación de Streamlit para Ciencia de Datos, IA y ML")

# Carga de datos (ejemplo con el dataset Iris)
@st.cache_data
def load_data():
    iris = load_iris(as_frame=True)
    return iris.data, iris.target

data, target = load_data()
df = pd.concat([data, target.rename("target")], axis=1)

# Sección 1: Visualización de datos
st.header("1. Visualización de Datos")
st.write("Explora el dataset Iris con diferentes visualizaciones.")

# Selección de características para visualizar
features = st.multiselect("Selecciona las características", df.columns[:-1], default=df.columns[:-1])
if features:
    st.write(df[features].describe())
    fig = px.scatter(df, x=features[0], y=features[1], color="target", title="Scatter Plot")
    st.plotly_chart(fig)

# Sección 2: Interactividad con datos
st.header("2. Interactividad con Datos")
st.write("Filtra el dataset por rango de valores.")

# Filtro de datos
min_val = st.slider("Valor mínimo", float(df[features[0]].min()), float(df[features[0]].max()), value=float(df[features[0]].min()))
max_val = st.slider("Valor máximo", float(df[features[0]].min()), float(df[features[0]].max()), value=float(df[features[0]].max()))
filtered_df = df[(df[features[0]] >= min_val) & (df[features[0]] <= max_val)]

st.write(f"Registros filtrados: {len(filtered_df)}")
st.dataframe(filtered_df)

# Sección 3: Integración de ML
st.header("3. Integración de ML")
st.write("Entrena un modelo de clasificación y realiza predicciones.")

# Entrenamiento del modelo (solo si se presiona el botón)
if st.button("Entrenar modelo"):
    X = df.drop("target", axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    st.success("Modelo entrenado exitosamente!")

# Predicción con el modelo
if "model" in locals():
    st.subheader("Realiza una predicción")
    st.write("Ingresa los valores de las características para predecir la especie de Iris.")

    # Widgets para ingresar valores
    sepal_length = st.number_input("Largo del sépalo", min_value=0.0, max_value=10.0, value=5.0)
    sepal_width = st.number_input("Ancho del sépalo", min_value=0.0, max_value=10.0, value=3.0)
    petal_length = st.number_input("Largo del pétalo", min_value=0.0, max_value=10.0, value=1.0)
    petal_width = st.number_input("Ancho del pétalo", min_value=0.0, max_value=10.0, value=0.2)

    # Realizar predicción
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)
    species = ["Setosa", "Versicolor", "Virginica"]
    st.write(f"La especie predicha es: {species[prediction[0]]}")

# Sección 4: Ejemplo de IA: Clasificación de Texto
st.header("4. Ejemplo de IA: Clasificación de Texto")
st.write("Usa un modelo preentrenado para clasificar texto (ejemplo simplificado).")

# Ejemplo de clasificación de texto (usando un modelo dummy por simplicidad)
def classify_text(text):
    # Este es un ejemplo dummy; en la práctica, usarías un modelo preentrenado como BERT
    if "positivo" in text.lower():
        return "Positivo"
    elif "negativo" in text.lower():
        return "Negativo"
    else:
        return "Neutral"

text_input = st.text_input("Ingresa un texto para clasificar")
if text_input:
    result = classify_text(text_input)
    st.write(f"Clasificación: {result}")

# Sección 5: Información adicional
st.header("5. Información Adicional")
st.write("Para más ejemplos y funcionalidades, consulta la documentación oficial de Streamlit o el repositorio del libro 'Streamlit for Data Science'.")
st.markdown("---")
st.write("Desarrollado con ❤️ usando Streamlit.")
