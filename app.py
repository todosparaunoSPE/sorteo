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


page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #e5e5f7;
opacity: 0.8;
background: repeating-linear-gradient( -45deg, #444cf7, #444cf7 5px, #e5e5f7 5px, #e5e5f7 25px );    
</sytle>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


# Título de la app
#st.title("Simulación de Sorteo por Folios")


# Título en rojo utilizando HTML
st.markdown(
    """
    <h1 style='color: black;'>Simulación de Sorteo por Folios</h1>
    """,
    unsafe_allow_html=True
)

# Mostrar el texto en negro antes del cargador de archivos
st.markdown(
    """
    <h2 style='color: black;'>Carga el archivo de Excel con los nombres y folios</h2>
    """,
    unsafe_allow_html=True
)

# Cargar el archivo de Excel
#uploaded_file = st.file_uploader("Carga el archivo de Excel con los nombres y folios", type=["xlsx"])

# Cargador de archivos
uploaded_file = st.file_uploader("", type=["xlsx"])  # La etiqueta está vacía

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
