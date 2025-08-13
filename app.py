import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pd.read_pickle('movies.pkl')
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

st.title('MovieRec: Content-Based Movie Recommender')
st.write('Discover new movies based on one you already love!')

movie_list = movies['title'].values
selected_movie = st.selectbox('Choose a movie:', movie_list)

if st.button('Recommend'):
    idx = movies[movies['title'] == selected_movie].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    st.subheader('Recommended movies:')
    for i in movie_indices:
        st.write(movies['title'].iloc[i])

st.markdown('''---
**How does the recommendation work?**

Recommendations are made based on the content similarity between movies. The system combines information from genre, cast, director, and storyline for each movie, creating a unique textual representation. This representation is transformed into vectors using the TF-IDF technique, and the similarity between movies is calculated using the cosine metric. When you select a movie, the system returns the 5 most similar titles according to this calculation.
---''')
