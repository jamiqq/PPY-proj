import bcrypt
import sqlite3

DB_PATH = "./databases/users.db"

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def verify_password(input_password, stored_hash):
    return bcrypt.checkpw(input_password.encode(), stored_hash)

def register_user(username, password):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                      (username, hash_password(password)))
            conn.commit()
            return True, "User registered successfully."
        except sqlite3.IntegrityError:
            return False, "Username already exists."

def login_user(username, password):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        if result and verify_password(password, result[0]):
            return True, "Login successful."
        else:
            return False, "Invalid username or password."
