import sqlite3

def setup_database():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()

    # Create the movies table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_name TEXT NOT NULL,
        genre TEXT NOT NULL,
        mood_tag TEXT NOT NULL,
        rating REAL NOT NULL
    )
    """)

    # Insert 50 movies into the database
    movies = [
        # Happy mood
        ("The Lion King", "Animation", "happy", 8.5),
        ("Toy Story", "Animation", "happy", 8.3),
        ("Finding Nemo", "Animation", "happy", 8.1),
        ("Zootopia", "Animation", "happy", 8.0),
        ("Shrek", "Animation", "happy", 7.9),
        ("Kung Fu Panda", "Animation", "happy", 7.8),
        ("The Secret Life of Pets", "Animation", "happy", 6.5),
        ("Despicable Me", "Animation", "happy", 7.6),
        ("Lego Movie", "Animation", "happy", 7.7),
        ("Ratatouille", "Animation", "happy", 8.0),

        # Sad mood
        ("The Shawshank Redemption", "Drama", "sad", 9.3),
        ("The Pursuit of Happyness", "Drama", "sad", 8.0),
        ("A Beautiful Mind", "Drama", "sad", 8.2),
        ("Forrest Gump", "Drama", "sad", 8.8),
        ("Million Dollar Baby", "Drama", "sad", 8.1),
        ("The Fault in Our Stars", "Drama", "sad", 7.7),
        ("Me Before You", "Romance", "sad", 7.4),
        ("Cast Away", "Adventure", "sad", 7.8),
        ("My Sister's Keeper", "Drama", "sad", 7.4),
        ("Schindler's List", "Biography", "sad", 9.0),

        # Adventurous mood
        ("Interstellar", "Sci-Fi", "adventurous", 8.6),
        ("Guardians of the Galaxy", "Action", "adventurous", 8.0),
        ("Mad Max: Fury Road", "Action", "adventurous", 8.1),
        ("Avengers: Endgame", "Action", "adventurous", 8.4),
        ("Inception", "Sci-Fi", "adventurous", 8.8),
        ("Jurassic Park", "Adventure", "adventurous", 8.1),
        ("The Dark Knight", "Action", "adventurous", 9.0),
        ("Pirates of the Caribbean", "Adventure", "adventurous", 8.0),
        ("The Martian", "Sci-Fi", "adventurous", 8.0),
        ("Spider-Man: No Way Home", "Action", "adventurous", 8.4),

        # Romantic mood
        ("Titanic", "Romance", "romantic", 7.8),
        ("The Notebook", "Romance", "romantic", 7.9),
        ("Pride & Prejudice", "Romance", "romantic", 7.8),
        ("La La Land", "Romance", "romantic", 8.0),
        ("The Fault in Our Stars", "Drama", "romantic", 7.7),
        ("Crazy Rich Asians", "Comedy", "romantic", 7.0),
        ("The Vow", "Romance", "romantic", 6.8),
        ("50 First Dates", "Comedy", "romantic", 6.8),
        ("A Star is Born", "Romance", "romantic", 7.6),
        ("Notting Hill", "Romance", "romantic", 7.2),

        # Additional mixed entries
        ("Coco", "Animation", "happy", 8.4),
        ("Soul", "Animation", "happy", 8.1),
        ("Life is Beautiful", "Drama", "sad", 8.6),
        ("The Grand Budapest Hotel", "Comedy", "happy", 8.1),
        ("How to Train Your Dragon", "Animation", "happy", 8.1),
        ("Dangal", "Biography", "adventurous", 8.4),
        ("Slumdog Millionaire", "Drama", "sad", 8.0),
        ("Eternal Sunshine of the Spotless Mind", "Romance", "romantic", 8.3),
        ("The Social Network", "Biography", "adventurous", 7.7),
        ("Inside Out", "Animation", "happy", 8.1)
    ]
    cursor.executemany("INSERT INTO movies (movie_name, genre, mood_tag, rating) VALUES (?, ?, ?, ?)", movies)

    # Commit and close connection
    connection.commit()
    connection.close()
    print("Database setup complete! 50 movies added.")

if __name__ == "__main__":
    setup_database()
