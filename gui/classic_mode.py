import tkinter as tk
from tkinter import ttk, messagebox
from db_handling.words_db import get_random_word

class ClassicGameWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Classic Game Mode")
        self.geometry("400x300")
        self.resizable(False, False)

        self.category_var = tk.StringVar()
        self.difficulty_var = tk.StringVar()

        self.word = None
        self.hidden_word = None

        self.create_widgets()
        self.load_categories()

    def create_widgets(self):
        ttk.Label(self, text="Select Category:").pack(pady=(20,5))
        self.category_cb = ttk.Combobox(self, textvariable=self.category_var, state="readonly")
        self.category_cb.pack()

        ttk.Label(self, text="Select Difficulty:").pack(pady=(20,5))
        self.difficulty_cb = ttk.Combobox(self, textvariable=self.difficulty_var, state="readonly")
        self.difficulty_cb['values'] = ('Easy', 'Medium', 'Hard')
        self.difficulty_cb.pack()

        self.start_btn = ttk.Button(self, text="Start Game", command=self.start_game)
        self.start_btn.pack(pady=20)

        self.word_label = ttk.Label(self, text="", font=("Courier", 24))
        self.word_label.pack(pady=10)

    def load_categories(self):
        # Load categories directly from DB for dropdown
        import sqlite3
        conn = sqlite3.connect("./databases/words.db")
        c = conn.cursor()
        c.execute("SELECT name FROM categories ORDER BY name")
        categories = [row[0] for row in c.fetchall()]
        conn.close()

        self.category_cb['values'] = categories
        if categories:
            self.category_cb.current(0)
        self.difficulty_cb.current(0)

    def start_game(self):
        difficulty = self.difficulty_var.get()
        category = self.category_var.get()

        word = get_random_word(difficulty, category)
        if not word:
            messagebox.showerror("No words found", "No words found for the selected category and difficulty.")
            return

        self.word = word.lower()
        self.hidden_word = ['_' if ch.isalpha() else ch for ch in self.word]
        self.update_word_display()

        # Disable controls during game
        self.category_cb.config(state='disabled')
        self.difficulty_cb.config(state='disabled')
        self.start_btn.config(state='disabled')

        # Hook guess input here or link to your existing guess logic

    def update_word_display(self):
        display = ' '.join(self.hidden_word)
        self.word_label.config(text=display)
