import pickle
import streamlit as st
import requests

# Function to fetch movie poster using OMDb API
def fetch_poster(movie_title):
    api_key = ""  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['Response'] == "True" and 'Poster' in data:
        return data['Poster']  # URL of the poster
    else:
        # Fallback to a placeholder image if no poster is found
        return "download.jpg"

# Function to recommend movies based on similarity
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []

    for i in distances[1:6]:  # Fetch top 5 recommendations
        movie_title = movies.iloc[i[0]].title
        recommended_movies_name.append(movie_title)
        recommended_movies_poster.append(fetch_poster(movie_title))

    return recommended_movies_name, recommended_movies_poster

# Streamlit UI
st.header("Movie Recommendation System Using Machine Learning")

# Load pre-trained data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similary.pkl', 'rb'))

# Dropdown to select a movie
movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

# Show recommendations on button click
if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)

    # Display recommendations in a row of 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])
    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])

# Sidebar credits
st.sidebar.markdown("--------")
st.sidebar.markdown("Developed By [Sachin Borse]")