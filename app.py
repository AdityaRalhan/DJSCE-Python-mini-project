import sqlite3
import streamlit as st

# Function to fetch movie recommendations based on mood
def fetch_movies_by_mood(mood):
    try:
        connection = sqlite3.connect("movies.db")
        cursor = connection.cursor()

        # Query to fetch movies that match the mood, including the movie URL
        query = "SELECT movie_name, genre, rating, imdb_url FROM movies WHERE mood_tag = ? ORDER BY rating DESC"
        cursor.execute(query, (mood.lower(),))
        movies = cursor.fetchall()
        connection.close()

        return movies
    except sqlite3.Error as e:
        st.error(f"Database error: {e}")
        return None


# Add custom CSS styles using st.markdown
st.markdown("""
    <style>
        /* General Styling */ 
       
        .stApp {

            color: white;  /* Ensure text is black */
        
        }

        /* Title Styling */
        h1 {
            text-align: center;
            color: #007BFF;
        }

        /* Sidebar Styling */
        .css-1d391kg {
            background-color: #4CAF50;
            color: white;
        }

        .stSidebar .sidebar-content {
            background-color: #f0f0f0;
        }

        /* Movie Recommendation Styling */
        .movie-card {
            background-color: transparent; /* No background color */
            border: none; /* No border */
            margin-bottom: 20px;
            padding: 15px;  /* Increased padding for better spacing */
        }

        .movie-card h3 {
            margin: 0;
            color: #007BFF;
            font-size: 22px;  /* Increased movie name font size */
        }

        .movie-card p {
            font-size: 18px;  /* Increased description font size */
            color: white; /* Text color for better contrast */
        }

        /* Button Styling */
        .stButton>button {
            background-color: #007BFF;
            color: white;
            font-weight: bold;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit App
st.title("Mood-Based Movie Recommendation System 🎥")

st.sidebar.header("How are you feeling today?")
user_mood = st.sidebar.radio("Select your mood:", ["Happy", "Sad", "Adventurous", "Romantic"])

if st.sidebar.button("Get Recommendations"):
    st.subheader(f"Movie Recommendations for mood: {user_mood}")
    recommendations = fetch_movies_by_mood(user_mood)
    
    if recommendations:
        for name, genre, rating, imdb_url in recommendations:
            st.markdown(f"""
            <div class="movie-card">
                <h3>{name}</h3>
                <p><strong>Genre:</strong> {genre} <br>
                <strong>Rating:</strong> {rating}</p>
                <p><a href="{imdb_url}" target="_blank" style="color: #007BFF;">Click here for details</a></p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write(f"No movies found for the mood '{user_mood}'.")
