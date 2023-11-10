import pandas as pd
import plotly.express as px
import streamlit as st


# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Cuadro de Mandos de Venta de Coches')

# Creamos checkbox para evalurar el clic y pintar histograma
build_histogram = st.checkbox('Construir un histograma')

# Creamos checkbox para evalurar el clic y pintar gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Evaluamos clic del check de histograma
if build_histogram:
    # Mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de autos')

    # Crear histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # Mostrar gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True,  color_discrete_sequence=['indianred'])


# Evaluamos clic del check de gráfico de dispersión
if build_scatter:
    # Mensaje
    st.write('Creación de un gráfico de dispersión para \
             el conjunto de datos de anuncios de venta de autos')

    # Crear gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="type")

    # Mostrar gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
