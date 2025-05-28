import sqlite3
import random

DB_PATH = "./databases/words.db"

# Selecting random word (using ORDER BY RANDOM() LIMIT 1 + applied filters and category) from words database
def get_random_word(difficulty=None, category=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    query = """
    SELECT w.word FROM words w
    JOIN categories c ON w.category_id = c.id
    """

    params = []
    filters = []

    if difficulty:
        filters.append("w.difficulty =?")
        params.append(difficulty)
    if category:
        filters.append("c.name =?")
        params.append(category)

    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += "ORDER BY RANDOM() LIMIT 1"

    c.execute(query, params)
    row = c.fetchone()
    conn.close()

    if row:
        return row[0]
    return None

# Adding category to category table
def add_category(name):
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()
    try:
        curs.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

# Selecting categories from categories table
def get_categories():
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()
    curs.execute("SELECT id, name FROM categories")
    categories = curs.fetchall()
    conn.close()
    return categories

# Adding word to words table
def add_word(word, difficulty, category_id):
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()
    curs.execute(
        "INSERT INTO words (word, difficulty, category_id) VALUES (?, ?, ?)",
        (word, difficulty, category_id),
    )
    conn.commit()
    conn.close()
