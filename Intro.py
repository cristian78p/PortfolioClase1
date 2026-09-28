import os
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

def cargar_imagen(nombre_base, width=200):
    """Busca y carga la imagen probando extensiones comunes (.jpg, .png, .webp)"""
    for ext in ['.jpg', '.png', '.webp']:
        ruta = nombre_base + ext
        if os.path.exists(ruta):
            try:
                st.image(Image.open(ruta), width=width)
                return
            except Exception:
                pass
    st.warning(f"Imagen '{nombre_base}.*' no encontrada.")

# Distribución en 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    # Página 1 (img1)
    st.subheader("¿Qué fruta es más parecida?")
    cargar_imagen('img1')
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
    cargar_imagen('img2')
    st.write(
        "Una herramienta visual para comprender el algoritmo de optimización central del aprendizaje automático. "
        "Muestra cómo los parámetros (tasa de aprendizaje) afectan la convergencia o divergencia hacia el mínimo "
        "de una función de costo en 3D."
    )
    st.write("Acceso: [Enlace](https://pruebaclase3-mhtdeyvhuuaqphi6poqnql.streamlit.app/)")

    # Página 3 (img3)
    st.subheader("Detector de Anomalías: Lógica + Big-O")
    cargar_imagen('img3')
    st.write(
        "Un benchmark visual que compara dos enfoques para detectar anomalías "
        "(umbrales lógicos sencillos vs. vectorización eficiente con NumPy), "
        "destacando la importancia de la complejidad computacional (Big-O) y el rendimiento en ciencia de datos."
    )
    st.write("Acceso: [Enlace](https://pruebaclase4-qemcmdey4kqfwyudxrmyaz.streamlit.app/)")

    # Página 4 (img4)
    st.subheader("Estructura y Preparación de Datos")
    cargar_imagen('img4')
    st.write(
        "**Módulo 5 (IoT):** Una interfaz para configurar y explorar un dataset sintético de sensores IoT. "
        "Se enfoca en la 'preparación' de datos: lidiar con valores faltantes, valores atípicos (outliers) "
        "y visualización de la estructura de la tabla de datos."
    )
    st.write("Acceso: [Enlace](https://pruebaclase5-txf23tvysqr5evhsjpqrsm.streamlit.app/)")

with col2:
    # Página 5 (img5)
    st.subheader("Nivel de Ríos y Quebradas")
    cargar_imagen('img5')
    st.write(
        "**CORNARE:** Un panel de control (dashboard) para el monitoreo en tiempo real de datos hidrológicos (nivel de ríos). "
        "Utiliza visualización de series temporales y ubicación geográfica para la gestión de recursos naturales."
    )
    st.write("Acceso: [Enlace](https://pruebaclase6-dnd8mcyzhgqsvtfrhmr7wr.streamlit.app/)")

    # Página 6 (img6)
    st.subheader("Regresión: Conceptos Clave")
    cargar_imagen('img6')
    st.write(
        "**(Vivienda):** Una herramienta interactiva para ajustar modelos de regresión lineal (simple y múltiple) "
        "sobre datos reales de vivienda en California, explorando visualmente la función de costo y el error (MSE)."
    )
    st.write("Acceso: [Enlace](https://pruebaclase7-lmnmxgmqg4qjeph5djzmrb.streamlit.app/)")

    # Página 7 (img7)
    st.subheader("Series de Tiempo - Sensor IoT")
    cargar_imagen('img7')
    st.write(
        "Una aplicación interactiva para descomponer y analizar series temporales simuladas (temperatura). "
        "Permite ajustar componentes como tendencia, estacionalidad y ruido, esenciales para el pronóstico."
    )
    st.write("Acceso: [Enlace](https://pruebaclase8-5ttjmlwuehhzwbvfd3ws35.streamlit.app/)")

    # Página 8 (img8)
    st.subheader("Calidad del Aire - CORNARE")
    cargar_imagen('img8')
    st.write(
        "**(MARCO):** Una interfaz que permite cargar modelos predictivos (`.pkl`) para realizar pronósticos "
        "de calidad del aire (PM2.5 y PM10) en una región específica, enfocada en la implementación de modelos entrenados."
    )
    st.write("Acceso: [Enlace](https://pruebaclase9-hb8hjs6vhfxrcc4qpx8lt5.streamlit.app/)")

with col3:
    # Página 9 (img9)
    st.subheader("Predictor de Sensación Térmica")
    cargar_imagen('img9')
    st.write(
        "Una aplicación práctica que conecta con una base de datos de tiempo real (InfluxDB) "
        "para obtener datos de sensores IoT y entrenar un modelo de regresión lineal que predice la sensación térmica, "
        "ilustrando el flujo completo de datos."
    )
    st.write("Acceso: [Enlace](https://pruebaclase10-ewjudmlherrlkqcbqftasq.streamlit.app/)")

    # Página 10 (img10)
    st.subheader("¿Lloverá mañana?")
    cargar_imagen('img10')
    st.write(
        "**Regresión Logística Interactiva:** Una herramienta interactiva para explorar la clasificación binaria. "
        "Muestra la función sigmoide, el umbral de clasificación y un gráfico de dispersión para predecir un resultado categórico (lluvia: sí/no)."
    )
    st.write("Acceso: [Enlace](https://pruebaclase12-etebhnappweghuw8dtbnafs.streamlit.app/)")

    # Página 11 (img11)
    st.subheader("Explora KNN en Suelos")
    cargar_imagen('img11')
    st.write(
        "**(AGROSAVIA):** Esta página es un caso de estudio completo y avanzado que aplica el algoritmo K-NN (K-Nearest Neighbors) "
        "a datos abiertos reales. El objetivo es clasificar la fertilidad del suelo (baja, media, alta) "
        "basándose en características como materia orgánica y fósforo."
    )
    st.write("Acceso: [Enlace](https://pruebaclase13-fhkzvagse89jktjnxhvfme.streamlit.app/)")
