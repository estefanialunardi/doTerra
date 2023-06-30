import streamlit as st
import pandas as pd

st.set_page_config(page_title='Conheça os óleos dōTERRA', page_icon=('oleos.png'), layout="centered", initial_sidebar_state="auto", menu_items=None)


st.markdown(
    """
    <style>
    .body {
    color: #662d91;
    background-color: #e0d2e0;
    /* font-size: 40px; */
    justify-content: center
}

.stButton>button{
    color: #662d91;
    backgroud-color: #e0d2e0;
    justify-content: center
    box-sizing: 5%;
    height: 2em;
    width: 20em;
    font-size:16px;
    border: 2px solid;
    border-radius: 5px;
    padding: 30px;
}

.stTextInput>div>div>input {
    color: #000000;
}

.fullScreenFrame > div {
    display: flex;
    justify-content: center;
}

.center {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
    </style>
    """,
    unsafe_allow_html=True)

st.header("""Descubra o óleo ideal para você""")

st.write(""" 👇 Escreva a sua queixa para descobrir o óleo com os benefícios necessários""")


lavender = ['dores de cabeça', 'dor de cabeça', 'enxaquecas', 'enxaqueca', 'tensão muscular', 'queimadura', 'queimaduras', 'acne', 'espinhas', 'espinha', 'tensões musculares', 'irritação na pele', 'irritações na pele', 'irritação de pele', 'irritações de pele', 'insônia', 'insonia', 'estresse', 'stresse', 'depressao', 'depressão']
lemon =  ['gripe', 'gripes', 'resfriado', 'resfriados', 'nariz entupido', 'congestão', 'constipação', 'dor de garganta', 'dores de garganta', 'inflamação de garganta', 'mau humor', 'mau-humor', 'tristeza']
peppermint = ['nausea', 'nauseas', 'náusea', 'náuseas', 'dor de barriga', 'dores de barriga', 'dores abdominais', 'dor abdominal', 'diarreia', 'colon irritavel', 'cólon irritável', 'intestino irritavel', 'intestino irritável', 'dor muscular', 'dores musculares', 'dor de cabeça', 'dores de cabeça', 'dor de cabeca', 'dores de cabeca', 'repelente', 'falta de concentração', 'falta de concentracao', 'nariz entupido', 'congestão nasal']
oils = [lavender, lemon, peppermint]
images = {lavender: 'lavanda-1.jpg', lemon: 'lemon.jpg', peppermint: 'peppermint.jpg' }

complaint= st.text_input('Escreva sua queixa', placeholder= 'dor de cabeça').lower()

for oil in oils:
    if complaint in oil:
        st.text(oil.upper())
        st.image(images[oil])

        st.success("Este é o óleo ideal para você!")

        st.balloons()

