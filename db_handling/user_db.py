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
            c.execute("INSERT INTO users (username, password_hash, games_played, games_won, games_lost) VALUES (?, ?, 0, 0, 0)",
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

def get_user_stats(username):
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()
    curs.execute("SELECT games_played, games_won, games_lost FROM users WHERE username = ?", (username,))
    row = curs.fetchone()
    conn.close()

    if row:
        games_played, games_won, games_lost = row
        return{
            "games_played": games_played,
            "games_won": games_won,
            "games_lost": games_lost,
            "win_rate": round((games_won / games_played * 100) if games_played > 0 else 0, 2)
        }
    return None

def update_user_stats(username, won):
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()
    curs.execute("SELECT games_played, games_won, games_lost FROM users WHERE username = ?", (username,))
    row = curs.fetchone()
    if row:
        player_count, won_count, lost_count = row
        player_count += 1
        if won:
            won_count += 1
        else:
            lost_count += 1
        curs.execute('''
        UPDATE users
        SET games_played = ?, games_won = ?, games_lost = ?
        WHERE username = ?
        ''', (player_count, won_count, lost_count, username))
        conn.commit()
    conn.close()