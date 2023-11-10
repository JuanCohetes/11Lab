import streamlit as st
from PIL import Image

st.title("Mi primera app")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('medellin.jpg')

st.image(image, caption='Calles de Medellin')

texto = st.text_input('Nombre de mi barrio', 'Este es mi barrio')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')
  
with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Estrato socioeconomico", ('1', '2,'3','4','5'))
    if modo == '1':
       st.write('La vista es fundamental para tu interfaz')
    if modo == '2':
       st.write('La audición es fundamental para tu interfaz')
    if modo == '3':
       st.write('El tacto es fundamental para tu interfaz')
    if modo == '4':
       st.write('El tacto es fundamental para tu interfaz')   
    if modo == '5':
       st.write('El tacto es fundamental para tu interfaz')
