import tkinter as tk
from tkinter import ttk, messagebox
from db_handling.words_db import *

class CategoryWordUploader(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.cat_dict = None
        self.controller = controller

        ttk.Label(self, text="Create New Category").pack(pady=5)
        self.new_cat_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.new_cat_var).pack()
        ttk.Button(self, text="Add Category", command=self.add_category).pack(pady=5)

        ttk.Label(self, text="Add New Word").pack(pady=10)

        self.word_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.word_var).pack()

        ttk.Label(self, text="Difficulty").pack()
        self.diff_var = tk.StringVar(value="Easy")
        ttk.Combobox(self, values=["Easy", "Medium", "Hard"], textvariable=self.diff_var).pack()

        ttk.Label(self, text="Category").pack()
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(self, textvariable=self.category_var)
        self.category_combo.pack()

        ttk.Button(self, text="Add Word", command=self.add_word).pack(pady=10)

        self.refresh_categories()

        ttk.Button(self, text="Back to Menu", command=lambda: ( controller.show_frame("MainMenu"))).pack(pady=10)

    def refresh_categories(self):
        categories = get_categories()
        self.cat_dict = {name: cid for cid, name in categories}
        self.category_combo['values'] = list(self.cat_dict.keys())
        if categories:
            self.category_combo.current(0)

    def add_category(self):
        cat_name = self.new_cat_var.get().strip()
        if not cat_name:
            messagebox.showwarning("Input error", "Please enter a category name.")
            return
        add_category(cat_name)
        messagebox.showinfo("Success", f"Category '{cat_name}' added.")
        self.new_cat_var.set("")
        self.refresh_categories()

    def add_word(self):
        word = self.word_var.get().strip()
        difficulty = self.diff_var.get()
        category_name = self.category_var.get()

        if not word:
            messagebox.showwarning("Input error", "Please enter a word.")
            return
        if category_name not in self.cat_dict:
            messagebox.showwarning("Input error", "Please select a valid category.")
            return

        category_id = self.cat_dict[category_name]
        add_word(word, difficulty, category_id)
        messagebox.showinfo("Success", f"Word '{word}' added to '{category_name}'.")
        self.word_var.set("")
