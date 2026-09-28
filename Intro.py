import streamlit as st
from PIL import Image

st.title("Laboratorios y Prácticas de Inteligencia Artificial")

with st.sidebar:
    st.subheader("Acerca de las Prácticas")
    parrafo = (
        "Este espacio recopila una serie de herramientas interactivas, "
        "modelos de Machine Learning, análisis de datos y sistemas IoT "
        "diseñados para comprender de forma práctica los conceptos clave de la IA."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# Distribución en 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    # Página 1 (img1)
    st.subheader("¿Qué fruta es más parecida?")
    try:
        st.image(Image.open('img1.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img1.png' no encontrada.")
    st.write(
        "**Similaridad Vectorial mediante Distancia Euclídea Directa.** "
        "Esta práctica enseña a medir la semejanza entre objetos del mundo real "
        "transformando sus características (peso, diámetro y dulzor) en vectores dentro de un espacio 3D. "
        "El script convierte los atributos en coordenadas y calcula la distancia euclídea en línea recta "
        "entre la fruta del usuario y las frutas conocidas."
    )
    st.write("Acceso: [Enlace](https://pruebaclase2-uyhmudfavyfszs4kbrvsgi.streamlit.app/)")

    # Página 2 (img2)
    st.subheader("Descenso de Gradiente Interactivo")
    try:
        st.image(Image.open('img2.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img2.png' no encontrada.")
    st.write(
        "Una herramienta visual para comprender el algoritmo de optimización central del aprendizaje automático. "
        "Muestra cómo los parámetros (tasa de aprendizaje) afectan la convergencia o divergencia hacia el mínimo "
        "de una función de costo en 3D."
    )
    st.write("Acceso: [Enlace](https://pruebaclase3-mhtdeyvhuuaqphi6poqnql.streamlit.app/)")

    # Página 3 (img3)
    st.subheader("Detector de Anomalías: Lógica + Big-O")
    try:
        st.image(Image.open('img3.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img3.png' no encontrada.")
    st.write(
        "Un benchmark visual que compara dos enfoques para detectar anomalías "
        "(umbrales lógicos sencillos vs. vectorización eficiente con NumPy), "
        "destacando la importancia de la complejidad computacional (Big-O) y el rendimiento en ciencia de datos."
    )
    st.write("Acceso: [Enlace](https://pruebaclase4-qemcmdey4kqfwyudxrmyaz.streamlit.app/)")

    # Página 4 (img4)
    st.subheader("Estructura y Preparación de Datos")
    try:
        st.image(Image.open('img4.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img4.png' no encontrada.")
    st.write(
        "**Módulo 5 (IoT):** Una interfaz para configurar y explorar un dataset sintético de sensores IoT. "
        "Se enfoca en la 'preparación' de datos: lidiar con valores faltantes, valores atípicos (outliers) "
        "y visualización de la estructura de la tabla de datos."
    )
    st.write("Acceso: [Enlace](https://pruebaclase5-txf23tvysqr5evhsjpqrsm.streamlit.app/)")

with col2:
    # Página 5 (img5)
    st.subheader("Nivel de Ríos y Quebradas")
    try:
        st.image(Image.open('img5.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img5.png' no encontrada.")
    st.write(
        "**CORNARE:** Un panel de control (dashboard) para el monitoreo en tiempo real de datos hidrológicos (nivel de ríos). "
        "Utiliza visualización de series temporales y ubicación geográfica para la gestión de recursos naturales."
    )
    st.write("Acceso: [Enlace](https://pruebaclase6-dnd8mcyzhgqsvtfrhmr7wr.streamlit.app/)")

    # Página 6 (img6)
    st.subheader("Regresión: Conceptos Clave")
    try:
        st.image(Image.open('img6.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img6.png' no encontrada.")
    st.write(
        "**(Vivienda):** Una herramienta interactiva para ajustar modelos de regresión lineal (simple y múltiple) "
        "sobre datos reales de vivienda en California, explorando visualmente la función de costo y el error (MSE)."
    )
    st.write("Acceso: [Enlace](https://pruebaclase7-lmnmxgmqg4qjeph5djzmrb.streamlit.app/)")

    # Página 7 (img7)
    st.subheader("Series de Tiempo - Sensor IoT")
    try:
        st.image(Image.open('img7.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img7.png' no encontrada.")
    st.write(
        "Una aplicación interactiva para descomponer y analizar series temporales simuladas (temperatura). "
        "Permite ajustar componentes como tendencia, estacionalidad y ruido, esenciales para el pronóstico."
    )
    st.write("Acceso: [Enlace](https://pruebaclase8-5ttjmlwuehhzwbvfd3ws35.streamlit.app/)")

    # Página 8 (img8)
    st.subheader("Calidad del Aire - CORNARE")
    try:
        st.image(Image.open('img8.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img8.png' no encontrada.")
    st.write(
        "**(MARCO):** Una interfaz que permite cargar modelos predictivos (`.pkl`) para realizar pronósticos "
        "de calidad del aire (PM2.5 y PM10) en una región específica, enfocada en la implementación de modelos entrenados."
    )
    st.write("Acceso: [Enlace](https://pruebaclase9-hb8hjs6vhfxrcc4qpx8lt5.streamlit.app/)")

with col3:
    # Página 9 (img9)
    st.subheader("Predictor de Sensación Térmica")
    try:
        st.image(Image.open('img9.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img9.png' no encontrada.")
    st.write(
        "Una aplicación práctica que conecta con una base de datos de tiempo real (InfluxDB) "
        "para obtener datos de sensores IoT y entrenar un modelo de regresión lineal que predice la sensación térmica, "
        "ilustrando el flujo completo de datos."
    )
    st.write("Acceso: [Enlace](https://pruebaclase10-ewjudmlherrlkqcbqftasq.streamlit.app/)")

    # Página 10 (img10)
    st.subheader("¿Lloverá mañana?")
    try:
        st.image(Image.open('img10.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img10.png' no encontrada.")
    st.write(
        "**Regresión Logística Interactiva:** Una herramienta interactiva para explorar la clasificación binaria. "
        "Muestra la función sigmoide, el umbral de clasificación y un gráfico de dispersión para predecir un resultado categórico (lluvia: sí/no)."
    )
    st.write("Acceso: [Enlace](https://pruebaclase12-etebhnappweghuw8dtbnafs.streamlit.app/)")

    # Página 11 (img11)
    st.subheader("Explora KNN en Suelos")
    try:
        st.image(Image.open('img11.png'), width=200)
    except FileNotFoundError:
        st.warning("Imagen 'img11.png' no encontrada.")
    st.write(
        "**(AGROSAVIA):** Esta página es un caso de estudio completo y avanzado que aplica el algoritmo K-NN (K-Nearest Neighbors) "
        "a datos abiertos reales. El objetivo es clasificar la fertilidad del suelo (baja, media, alta) "
        "basándose en características como materia orgánica y fósforo."
    )
    st.write("Acceso: [Enlace](https://pruebaclase13-fhkzvagse89jktjnxhvfme.streamlit.app/)")
