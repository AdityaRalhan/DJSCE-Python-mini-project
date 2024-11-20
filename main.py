from flask import Flask, request, jsonify
import sqlite3
import traceback

app = Flask(__name__)

# Function to fetch movie recommendations based on mood
def fetch_movies_by_mood(mood):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect("movies.db")
        cursor = connection.cursor()

        # Query to fetch movies that match the mood
        query = "SELECT movie_name, genre, rating FROM movies WHERE mood_tag = ? ORDER BY rating DESC"
        cursor.execute(query, (mood.lower(),))
        movies = cursor.fetchall()

        connection.close()

        # If no movies are found, return an empty list
        if not movies:
            return []

        return movies
    except sqlite3.Error as e:
        # Log and return an error message if database query fails
        print(f"Database error: {e}")
        print(traceback.format_exc())
        return None

@app.route("/recommend", methods=["GET"])
def recommend_movies():
    mood = request.args.get("mood")
    if not mood:
        # Return error if mood is not provided in the query parameter
        return jsonify({"error": "Mood not provided"}), 400

    movies = fetch_movies_by_mood(mood)

    # Handle the case where no movies are found or there's a database error
    if movies is None:
        return jsonify({"error": "Database error"}), 500
    elif not movies:
        return jsonify({"error": f"No movies found for mood '{mood}'"}), 404

    # Format the response to include movie details
    response = [{"name": name, "genre": genre, "rating": rating} for name, genre, rating in movies]
    
    # Return the list of movie recommendations as JSON
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
