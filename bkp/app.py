import streamlit as st
import pickle
import pandas as pd

# Carregar dados
movies = pd.read_pickle('movies.pkl')
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

st.title('MovieRec: Content-Based Movie Recommender')
st.write('Descubra novos filmes baseados em um filme que você já gosta!')

movie_list = movies['title'].values
selected_movie = st.selectbox('Escolha um filme:', movie_list)

if st.button('Recomendar'):
    idx = movies[movies['title'] == selected_movie].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    st.subheader('Filmes recomendados:')
    for i in movie_indices:
        st.write(movies['title'].iloc[i])
