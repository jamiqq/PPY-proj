import sqlite3 as s
import bcrypt

def user_connect():
    return s.connect("/databases/users.db")

user_conn = user_connect()
user_cursor = user_conn.cursor()

user_cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
''')

test_users = [
    ("admin", bcrypt.hashpw("123".encode(), bcrypt.gensalt())),
    ("user", bcrypt.hashpw("user".encode(), bcrypt.gensalt()))
]

for username, pwd_hash in test_users:
    try:
        user_cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, pwd_hash))
    except s.IntegrityError:
        pass

user_conn.commit()
user_conn.close()

def words_connect():
    return s.connect("./databases/words.db")

words_conn = words_connect()
words_cursor = words_conn.cursor()

words_cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
''')

words_cursor.execute('''
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        difficulty TEXT CHECK (difficulty IN ('Easy', 'Medium', 'Hard')) NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
''')

categories = ['Animals', 'Countries', 'Fruits']
for cat in categories:
    try:
        words_cursor.execute("INSERT INTO categories (name) VALUES (?)", (cat,))
    except s.IntegrityError:
        pass

words_cursor.execute("SELECT id, name FROM categories")
category_map = {name: id for id, name in words_cursor.fetchall()}

word_data = [
    ("dog", "Easy", "Animals"),
    ("elephant", "Medium", "Animals"),
    ("platypus", "Hard", "Animals"),
    ("france", "Easy", "Countries"),
    ("australia", "Medium", "Countries"),
    ("kazakhstan", "Hard", "Countries"),
    ("apple", "Easy", "Fruits"),
    ("pineapple", "Medium", "Fruits"),
    ("pomegranate", "Hard", "Fruits"),
]

for word, difficulty, category in word_data:
    cat_id = category_map[category]
    words_cursor.execute(
        "INSERT INTO words (word, difficulty, category_id) VALUES (?, ?, ?)",
        (word.lower(), difficulty, cat_id)
    )

words_conn.commit()
words_conn.close()