import sqlite3

def setup_database():
    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()

    # Create the movies table with an IMDb URL column
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_name TEXT NOT NULL,
        genre TEXT NOT NULL,
        mood_tag TEXT NOT NULL,
        rating REAL NOT NULL,
        imdb_url TEXT
    )
    """)

    # Insert 50 movies into the database with IMDb links
    movies = [
        # Happy mood
        ("The Lion King", "Animation", "happy", 8.5, "https://www.imdb.com/title/tt0110357/"),
        ("Toy Story", "Animation", "happy", 8.3, "https://www.imdb.com/title/tt0114709/"),
        ("Finding Nemo", "Animation", "happy", 8.1, "https://www.imdb.com/title/tt0266543/"),
        ("Zootopia", "Animation", "happy", 8.0, "https://www.imdb.com/title/tt2948356/"),
        ("Shrek", "Animation", "happy", 7.9, "https://www.imdb.com/title/tt0126029/"),
        ("Kung Fu Panda", "Animation", "happy", 7.8, "https://www.imdb.com/title/tt0441773/"),
        ("The Secret Life of Pets", "Animation", "happy", 6.5, "https://www.imdb.com/title/tt2709768/"),
        ("Despicable Me", "Animation", "happy", 7.6, "https://www.imdb.com/title/tt1323594/"),
        ("Lego Movie", "Animation", "happy", 7.7, "https://www.imdb.com/title/tt1490017/"),
        ("Ratatouille", "Animation", "happy", 8.0, "https://www.imdb.com/title/tt0382932/"),

        # Sad mood
        ("The Shawshank Redemption", "Drama", "sad", 9.3, "https://www.imdb.com/title/tt0111161/"),
        ("The Pursuit of Happyness", "Drama", "sad", 8.0, "https://www.imdb.com/title/tt0454921/"),
        ("A Beautiful Mind", "Drama", "sad", 8.2, "https://www.imdb.com/title/tt0268978/"),
        ("Forrest Gump", "Drama", "sad", 8.8, "https://www.imdb.com/title/tt0109830/"),
        ("Million Dollar Baby", "Drama", "sad", 8.1, "https://www.imdb.com/title/tt0405159/"),
        ("The Fault in Our Stars", "Drama", "sad", 7.7, "https://www.imdb.com/title/tt2582846/"),
        ("Me Before You", "Romance", "sad", 7.4, "https://www.imdb.com/title/tt2674426/"),
        ("Cast Away", "Adventure", "sad", 7.8, "https://www.imdb.com/title/tt0162222/"),
        ("My Sister's Keeper", "Drama", "sad", 7.4, "https://www.imdb.com/title/tt1078588/"),
        ("Schindler's List", "Biography", "sad", 9.0, "https://www.imdb.com/title/tt0108052/"),

        # Adventurous mood
        ("Interstellar", "Sci-Fi", "adventurous", 8.6, "https://www.imdb.com/title/tt0816692/"),
        ("Guardians of the Galaxy", "Action", "adventurous", 8.0, "https://www.imdb.com/title/tt2015381/"),
        ("Mad Max: Fury Road", "Action", "adventurous", 8.1, "https://www.imdb.com/title/tt1392190/"),
        ("Avengers: Endgame", "Action", "adventurous", 8.4, "https://www.imdb.com/title/tt1838556/"),
        ("Inception", "Sci-Fi", "adventurous", 8.8, "https://www.imdb.com/title/tt1375666/"),
        ("Jurassic Park", "Adventure", "adventurous", 8.1, "https://www.imdb.com/title/tt0107290/"),
        ("The Dark Knight", "Action", "adventurous", 9.0, "https://www.imdb.com/title/tt0468569/"),
        ("Pirates of the Caribbean", "Adventure", "adventurous", 8.0, "https://www.imdb.com/title/tt0325980/"),
        ("The Martian", "Sci-Fi", "adventurous", 8.0, "https://www.imdb.com/title/tt3659388/"),
        ("Spider-Man: No Way Home", "Action", "adventurous", 8.4, "https://www.imdb.com/title/tt10872600/"),

        # Romantic mood
        ("Titanic", "Romance", "romantic", 7.8, "https://www.imdb.com/title/tt0120338/"),
        ("The Notebook", "Romance", "romantic", 7.9, "https://www.imdb.com/title/tt0332280/"),
        ("Pride & Prejudice", "Romance", "romantic", 7.8, "https://www.imdb.com/title/tt0414387/"),
        ("La La Land", "Romance", "romantic", 8.0, "https://www.imdb.com/title/tt3783958/"),
        ("The Fault in Our Stars", "Drama", "romantic", 7.7, "https://www.imdb.com/title/tt2582846/"),
        ("Crazy Rich Asians", "Comedy", "romantic", 7.0, "https://www.imdb.com/title/tt3104988/"),
        ("The Vow", "Romance", "romantic", 6.8, "https://www.imdb.com/title/tt1606389/"),
        ("50 First Dates", "Comedy", "romantic", 6.8, "https://www.imdb.com/title/tt0343660/"),
        ("A Star is Born", "Romance", "romantic", 7.6, "https://www.imdb.com/title/tt1517451/"),
        ("Notting Hill", "Romance", "romantic", 7.2, "https://www.imdb.com/title/tt0125439/"),

        # Additional mixed entries
        ("Coco", "Animation", "happy", 8.4, "https://www.imdb.com/title/tt2380307/"),
        ("Soul", "Animation", "happy", 8.1, "https://www.imdb.com/title/tt2948372/"),
        ("Life is Beautiful", "Drama", "sad", 8.6, "https://www.imdb.com/title/tt0118799/"),
        ("The Grand Budapest Hotel", "Comedy", "happy", 8.1, "https://www.imdb.com/title/tt2278388/"),
        ("How to Train Your Dragon", "Animation", "happy", 8.1, "https://www.imdb.com/title/tt0892769/"),
        ("Dangal", "Biography", "adventurous", 8.4, "https://www.imdb.com/title/tt5074352/"),
        ("Slumdog Millionaire", "Drama", "sad", 8.0, "https://www.imdb.com/title/tt1010048/"),
        ("Eternal Sunshine of the Spotless Mind", "Romance", "romantic", 8.3, "https://www.imdb.com/title/tt0338013/"),
        ("The Social Network", "Biography", "adventurous", 7.7, "https://www.imdb.com/title/tt1285016/"),
        ("Inside Out", "Animation", "happy", 8.1, "https://www.imdb.com/title/tt2096673/")
    ]
    cursor.executemany("INSERT INTO movies (movie_name, genre, mood_tag, rating, imdb_url) VALUES (?, ?, ?, ?, ?)", movies)

    # Commit and close connection
    connection.commit()
    connection.close()
    print("Database setup complete! 50 movies added with IMDb links.")

if __name__ == "__main__":
    setup_database()
