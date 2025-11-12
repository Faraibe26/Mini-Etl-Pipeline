📘 Mini ETL Pipeline — Open Library Books Dataset
🧩 Overview

This project demonstrates a simple ETL (Extract–Transform–Load) workflow using Python.
It extracts book data from the Open Library API
, stores it in a local SQLite database, performs SQL queries for analysis, and exports the results to a CSV file for visualization.

⚙️ Tech Stack

Language: Python 3

Libraries: requests · sqlite3 · pandas

Database: SQLite

🚀 Features

Extracts 30 + book records from the Open Library API for three topics (Python, Data Science, Machine Learning).

Transforms raw JSON data into a structured format for database storage.

Loads data into SQLite and executes SQL queries to analyze author frequency and publication trends.

Exports the final dataset to books_export.csv for reporting or visualization.

📊 Results / Key Insights

Identified Charles Dickens (4×) as the most frequent author among sampled records.

Analyzed publication patterns spanning five centuries (1500s – 2000s).

Demonstrated a complete data pipeline from API → Database → Analysis → Export.

🧠 Learning Outcomes

Practiced API integration and data extraction in Python.

Designed database schemas and executed SQL queries for aggregation and filtering.

Strengthened understanding of ETL concepts and data workflow automation.

📂 Project Structure
mini_etl_pipeline/
│
├── mini_etl_pipeline.py     # main ETL script
├── books.db                 # SQLite database file
├── books_export.csv         # exported dataset
└── README.md                # documentation

🧰 How to Run

git clone https://github.com/<your-username>/mini_etl_pipeline.git

cd mini_etl_pipeline

pip install pandas requests

python mini_etl_pipeline.py
