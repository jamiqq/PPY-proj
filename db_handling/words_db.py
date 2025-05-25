import sqlite3
import random

def get_random_word(difficulty=None, category=None):
    conn = sqlite3.connect("./databases/words.db")
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

    c.execute(query, params)
    words = [row[0] for row in c.fetchall()]
    conn.close()

    if not words:
        return None
    return random.choice(words)