# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:40:07 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd
import random
import time

# Cargar la imagen
logo = 'logo.jpg'  # Asegúrate de que el archivo logo.jpg esté en el mismo directorio que tu script

# Mostrar la imagen con el tamaño deseado
try:
    st.image(logo, width=700)  # Ajusta el ancho según lo necesites
except Exception as e:
    st.error(f"Error al cargar la imagen: {e}")

# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Título en rojo utilizando HTML
st.markdown(
    """
    <h1 style='color: white;'>Simulación de Sorteo por Folios</h1>
    """,
    unsafe_allow_html=True
)

# Sección de ayuda en la barra lateral
st.sidebar.markdown(
    """
    ### Ayuda
    Esta aplicación permite realizar un sorteo de folios a partir de un archivo de Excel que contenga una lista de nombres y sus correspondientes folios.
    
    **Pasos para utilizar la aplicación:**
    1. **Carga el archivo de Excel:** Asegúrate de que el archivo contenga las columnas 'Nombre' y 'Folio'.
    2. **Iniciar el sorteo:** Haz clic en el botón "Iniciar sorteo". La aplicación simulará un desfile de folios durante unos momentos.
    3. **Ganador:** Al finalizar el sorteo, la aplicación mostrará el folio ganador junto con el nombre correspondiente.

    Si el archivo no cumple con los requisitos, se mostrará un mensaje de error.
    """,
    unsafe_allow_html=True
)

# Cargar el archivo de Excel
uploaded_file = st.file_uploader("Carga el archivo de Excel con los nombres y folios", type=["xlsx"])

if uploaded_file is not None:
    # Leer el archivo de Excel
    df = pd.read_excel(uploaded_file)
    
    # Verificar que las columnas necesarias estén presentes
    if 'Nombre' in df.columns and 'Folio' in df.columns:
        # Mostrar el contenido del archivo para confirmar
        st.write("Contenido del archivo:")
        st.dataframe(df)
        
        # Obtener la lista de folios
        folios = df['Folio'].tolist()
        
        # Espacio para mostrar el folio actual
        folio_display = st.empty()  # Esto crea un contenedor que se puede actualizar dinámicamente
        
        # Botón para iniciar el sorteo
        if st.button("Iniciar sorteo"):
            st.write("Iniciando sorteo...")
            folio_ganador = None  # Inicializar el folio ganador

            # Simular el "desfile" de folios
            for _ in range(50):  # Desfila 50 veces antes de elegir el ganador
                folio_actual = random.choice(folios)  # Escoge un folio al azar en cada iteración
                folio_display.markdown(f"### Folio: {folio_actual}")  # Actualiza dinámicamente el folio en pantalla
                time.sleep(0.1)  # Controla la velocidad de la animación
                folio_ganador = folio_actual  # Actualizar el folio ganador con el actual
            
            # Ahora, folio_ganador contendrá el último folio mostrado
            ganador = df[df['Folio'] == folio_ganador]  # Filtrar para obtener el nombre del ganador
            nombre_ganador = ganador['Nombre'].values[0] if not ganador.empty else "N/A"  # Manejo de caso vacío
            
            # Mostrar el ganador
            st.success(f"¡El ganador es: {nombre_ganador} con el folio {folio_ganador}!")
    else:
        st.error("El archivo debe contener las columnas 'Nombre' y 'Folio'.")
else:
    st.info("Por favor, carga un archivo de Excel.")
