import streamlit as st


#zscore = st.radio("Criterio de aceptabilidad", ["1.65 (Recomendado)", "2.0"], horizontal=True)
z_score=0
analito = 0
unidades = 0
nivel = 1
media_comparacion = 0
ds_comparacion = 0
criterio = 0
interpretacion = 0
   
analito = st.text_input("Ingresa el analito:")
if not analito:
    st.warning("¡El analito es obligatorio!")

unidades = st.text_input("Ingresa las unidades:")
if not unidades:
    st.warning("¡Las unidades son obligatorias!")

nivel = st.selectbox("Ingresa el nivel del control ", [1, 2, 3, "Bajo","Normal","Alto"])
if not nivel:
    st.warning("¡El nivel del control es obligatorio!")

media_comparacion = st.number_input("Ingresa la media del fabricante:", value=0.0)
if media_comparacion is None:
    st.warning("¡La media de comparación es obligatoria!")

ds_comparacion = st.number_input("Ingresa la desviación estándar del fabricante:", value=0.0)
if ds_comparacion is None:
    st.warning("¡La desviación estándar de comparación es obligatoria!")
