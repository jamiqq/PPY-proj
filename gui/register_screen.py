import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from db_handling.user_db import register_user
from gui.styles.sound_manager import play_sound_effect

class RegisterScreen(ttk.Frame):
    def __init__(self, parent, controller):
        # Initializes the registration screen with input fields and navigation buttons.
        super().__init__(parent)
        self.controller = controller

        self.configure(style="TFrame")

        title = ttk.Label(self, text="Register", style="Title.TLabel")
        title.pack(pady=20)

        lbl_username = ttk.Label(self, text="New Username", style="TLabel")
        lbl_username.pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        lbl_password = ttk.Label(self, text="New Password", style="TLabel")
        lbl_password.pack()
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack()

        btn_create = ttk.Button(self, text="Create Account", command=lambda: (play_sound(), self.register()), style="TButton")
        btn_create.pack(pady=10)

        btn_back = ttk.Button(self, text="Back to Login", command=lambda: (play_sound(), controller.show_frame("Login")), style="TButton")
        btn_back.pack()

    # Handles registration logic: creates a new user and navigates back to login on success.
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = register_user(username, password)
        if success:
            messagebox.showinfo("Success", message)
            self.controller.show_frame("Login")
        else:
            messagebox.showerror("Error", message)

# Plays a click sound effect when triggered.
def play_sound():
    play_sound_effect("assets/sfx/click.wav")
