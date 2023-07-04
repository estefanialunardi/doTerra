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


lavender = { 'nome': "Lavender", 'beneficios': ['dores de cabeça', 'dor de cabeça', 'enxaquecas', 'enxaqueca', 'tensão muscular', 'queimadura', 'queimaduras', 'acne', 'espinhas', 'espinha', 'tensões musculares', 'irritação na pele', 'irritações na pele', 'irritação de pele', 'irritações de pele', 'insônia', 'insonia', 'estresse', 'stresse', 'depressao', 'depressão'], 'image': 'lavanda-1.jpg'} 
lemon =  {'nome': 'Lemon', 'beneficios': ['gripe', 'gripes', 'resfriado', 'resfriados', 'nariz entupido', 'congestão', 'constipação', 'dor de garganta', 'dores de garganta', 'inflamação de garganta', 'mau humor', 'mau-humor', 'tristeza'], 'image': 'lemon.jpg'}
peppermint ={ 'nome': 'Pepppermint', 'beneficios': ['nausea', 'nauseas', 'náusea', 'náuseas', 'dor de barriga', 'dores de barriga', 'dores abdominais', 'dor abdominal', 'diarreia', 'colon irritavel', 'cólon irritável', 'intestino irritavel', 'intestino irritável', 'dor muscular', 'dores musculares', 'dor de cabeça', 'dores de cabeça', 'dor de cabeca', 'dores de cabeca', 'repelente', 'falta de concentração', 'falta de concentracao', 'nariz entupido', 'congestão nasal'],'image': 'peppermint.jpg'}

frankincense = { 'nome': "Frankincense", 'beneficios': ['cancer', 'câncer', 'rugas', 'sinais', 'problemas na pele', 'envelhecimento', 'ansiedade', 'nervosismo', 'hipertireoidismo', 'hipotireiodismo', 'tireoide', 'hipertensao', 'hipertensão', 'tonturas', 'hematomas', 'cicatriz', 'cicatrizes', 'machucados'], 'image': 'frankincense.jpg'} 
tangerine =  {'nome': 'Tangerine', 'beneficios': ['gripe', 'gripes', 'resfriado', 'resfriados', 'nariz entupido', 'congestão', 'constipação', 'muco', 'candida', 'cândida', 'irritacao de pele', 'irritação de pele', 'insonia', 'insônia', 'dificuldade para dormir', 'estresse', 'stress', 'depressao', 'depressão', 'mau humor', 'mau-humor', 'tristeza'], 'image': 'tangerine.jpg'}
melaleuca ={ 'nome': 'Melaleuca', 'beneficios': ['herpes', 'herpes zoster', 'infecções', 'infeccoes', 'fungos', 'infeccoes fungigcas', 'infecções fúngicas', 'vaginite', 'candidiase', 'candidíase', 'picadas', 'picadas de inseto', 'piolho', 'dor de ouvido', 'ansiedade', 'estresse', 'stress', 'bacterias', 'machucados'],'image': 'melaleuca.jpg'}

copaiba = { 'nome': "Copaiba", 'beneficios': ['dor', 'dores', 'fibromialgia', 'dor muscular', 'dores musculares', 'hernia' 'hérnia', 'hernia de disco', 'hérnia de disco', 'inflamacoes', 'inflamações', 'doenca autoimune', 'doença autoimune', 'cirrose', 'hepatite', 'TPM', 'sintomas de tpm'], 'image': 'copaiba.jpg'} 
breathe =  {'nome': 'Breathe', 'beneficios': ['gripe', 'gripes', 'resfriado', 'resfriados', 'nariz entupido', 'congestão', 'constipação','sinusite', 'rinite', 'asma', 'ronco', 'tosse', 'desidratacao', 'desidratação', 'problemas respiratorios', 'problemas respiratórios', 'enfisema'], 'image': 'breathe.png'}
balance ={ 'nome': 'Balance', 'beneficios': ['ansiedade', 'estresse', 'stress', 'medo', 'traume', 'raiva', 'asperger', 'sindrome de asperger', 'síndrome de asperger', 'falta de concentracao', 'falta de concentração', 'nervosismo', 'insonia', 'insônia', 'convulsao', 'convulsão', 'convulsões', 'convulsoes', 'epilepsia'],'image': 'balance.jpg'}

zengest = { 'nome': "ZenGest", 'beneficios': ['azia', 'colica', 'cólica', 'diarreia', 'constipacao', 'problemas digestivos', 'infeccoes alimentares', 'infecções alimentares', 'infeccao alimentar', 'infecção alimentar', 'intestino irritavel', 'intestino irritávle', 'sindrome do intestino irritavel', 'síndrome do intestino irritável'], 'image': 'zengest.jpg'} 
onguard =  {'nome': 'On Guard', 'beneficios': ['viroses', 'vírus', 'virus', 'cistite', 'gripe', 'gripes', 'resfriado', 'resfriados', 'h1n1', 'infeccoes', 'infecções', 'diabetes', 'colesterol', 'colesterol alto', 'arritmia'], 'image': 'onguard.jpg'}
deepblue ={ 'nome': 'Deep Blue', 'beneficios': ['dor', 'dores', 'tensao', 'tensão', 'caimbra', 'cãimbra', 'artrite', 'artrose', 'fibromialgia', 'dor nas costas', 'lupus', 'lúpus', 'inflamacoes', 'inflamações', 'tunel carpal','túnel carpal', 'dor muscular', 'dores musculares',],'image': 'deepblue.jpg'}

oils = [lavender, lemon, peppermint, frankincense, tangerine, melaleuca, copaiba, breathe, balance, zengest, onguard, deepblue]

complaint= st.text_input('Escreva sua queixa', placeholder= 'Ex: dor de cabeça').lower()

for oil in oils:
    if complaint in oil['beneficios']:
        st.text(oil['nome'])
        st.image(oil['image'])
        st.text('Saiba como adquirir este e outros óleos')
        st.success("Escolha o óleo ideal para você!")

        st.balloons()

