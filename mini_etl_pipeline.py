# Step 1: Import libraries
import requests
import sqlite3
import pandas as pd

#Step 2: Extract data from the Open library API
topics = ["science", "art", "history"]
books = []

for topic in topics:
    response = requests.get(f"https://openlibrary.org/subjects/{topic}.json")
    data = response.json()

    for doc in data["works"]:
        title = doc.get("title", "N/A")
        author_names = [author["name"] for author in doc.get("authors", [])]
        first_publish_year = doc.get("first_publish_year", "N/A")   
        subjects = doc.get("subject", [])
        books.append({
            "title": title,
            "author_names": ", ".join(author_names),
            "first_publish_year": first_publish_year,
            "subjects": ", ".join(subjects)
        })
# Step 3: Load data into a SQLite database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author_names TEXT,
        first_publish_year INTEGER,
        subjects TEXT
    )
''')    
for book in books:
    cursor.execute('''
        INSERT INTO books (title, author_names, first_publish_year, subjects)
        VALUES (?, ?, ?, ?)
    ''', (book["title"], book["author_names"], book["first_publish_year"], book["subjects"]))
conn.commit()       
print("Data successfully loaded into books.db")

#Step 4: Query and analyse data
# Re-open the connection for analysis
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

#  Count the number of books per subject
print("Number of books per subject:")
for row in cursor.execute('''
    SELECT subjects, COUNT(*) as book_count
    FROM books
    GROUP BY subjects
    ORDER BY book_count DESC
'''):
    print(f"{row[0]}: {row[1]}")
    
#Top 5 authors with the most books
print("\nTop 5 authors with the most books:")
for row in cursor.execute('''
    SELECT author_names, COUNT(*) as book_count
    FROM books
    GROUP BY author_names
    ORDER BY book_count DESC
    LIMIT 5
'''):
    print(f"{row[0]}: {row[1]}")

# Books published per decade
print("\nBooks published per decade:")
for row in cursor.execute('''
    SELECT (first_publish_year / 10) * 10 as decade, COUNT(*) as book_count
    FROM books
    WHERE first_publish_year IS NOT NULL
    GROUP BY decade
    ORDER BY decade
'''):
    print(f"{row[0]}s: {row[1]}")

conn.close()

