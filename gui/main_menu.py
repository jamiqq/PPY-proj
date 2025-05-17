# gui/main_menu.py
import tkinter as tk
from tkinter import messagebox

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="Main Menu", font=("Arial", 20))
        self.label.pack(pady=20)

        tk.Button(self, text="Play", width=20, command=self.play).pack(pady=5)
        tk.Button(self, text="Statistics", command=lambda: controller.show_frame("StatisticsScreen")).pack(pady=10)
        tk.Button(self, text="Add Category", width=20, command=self.add_category).pack(pady=5)
        tk.Button(self, text="Switch User", width=20, command=self.switch_user).pack(pady=5)
        tk.Button(self, text="Exit", width=20, command=self.controller.quit).pack(pady=5)

        self.user_label = tk.Label(self, text="", fg="gray")
        self.user_label.pack(pady=10)

    def tkraise(self, *args, **kwargs):
        # Override to update user display
        username = self.controller.get_user()
        self.user_label.config(text=f"Logged in as: {username}")
        super().tkraise(*args, **kwargs)

    def play(self):
        messagebox.showinfo("Play", "Play screen will go here.")

    def stats(self):
        messagebox.showinfo("Statistics", "Statistics screen will go here.")

    def add_category(self):
        messagebox.showinfo("Add Category", "Add category screen will go here.")

    def switch_user(self):
        self.controller.set_user(None)
        self.controller.show_frame("Login")
