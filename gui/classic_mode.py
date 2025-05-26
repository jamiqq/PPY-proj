import tkinter as tk
from tkinter import ttk, messagebox
from db_handling.words_db import get_random_word

class ClassicGameSetupScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="TFrame")
        self.controller = controller

        self.category_var = tk.StringVar()
        self.difficulty_var = tk.StringVar()

        # Container frame to centralize content
        container = ttk.Frame(self)
        container.pack(expand=True)

        # Title
        ttk.Label(container, text="Choose Game Options", style="Title.TLabel").pack(pady=20)

        # Category
        ttk.Label(container, text="Select Category:", style="TLabel").pack(pady=(10, 5))
        self.category_cb = ttk.Combobox(container, textvariable=self.category_var, state="readonly")
        self.category_cb.pack()

        # Difficulty
        ttk.Label(container, text="Select Difficulty:", style="TLabel").pack(pady=(10, 5))
        self.difficulty_cb = ttk.Combobox(container, textvariable=self.difficulty_var, state="readonly")
        self.difficulty_cb['values'] = ('Easy', 'Medium', 'Hard')
        self.difficulty_cb.pack()

        # Start button
        ttk.Button(container, text="Start Game", command=self.start_game).pack(pady=20)

        self.load_categories()

    def load_categories(self):
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
        category = self.category_var.get()
        difficulty = self.difficulty_var.get()

        word = get_random_word(difficulty, category)
        if not word:
            messagebox.showerror("No words", "No words found for selected options.")
            return

        # Pass the word to GameScreen and show it
        game_screen = self.controller.frames["GameScreen"]
        game_screen.set_word(word)
        self.controller.show_frame("GameScreen")
