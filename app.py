import streamlit as st
import requests

# Function to fetch movie recommendations from Flask API
def get_movie_recommendations(mood):
    url = f"http://127.0.0.1:5000/recommend?mood={mood}"
    try:
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            return data['error']
        else:
            recommendations = ""
            for movie in data:
                recommendations += f"**{movie['name']}** ({movie['genre']}) - Rating: {movie['rating']}\n"
            return recommendations
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Mood-Based Movie Recommendation System")

# Mood selection dropdown
mood = st.selectbox("How are you feeling today?", ["", "happy", "sad", "adventurous", "romantic"])

# Button to get movie recommendations
if st.button("Get Recommendations"):
    if mood:
        st.subheader(f"Recommendations for {mood} mood:")
        recommendations = get_movie_recommendations(mood)
        st.write(recommendations)
    else:
        st.warning("Please select a mood to get recommendations.")
