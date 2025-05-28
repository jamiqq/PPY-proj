from tkinter import messagebox
from tkinter import ttk
from db_handling.user_db import login_user
from gui.styles.sound_manager import play_sound_effect

class LoginScreen(ttk.Frame):
    def __init__(self, parent, controller):
        # Initializes the login screen with input fields and buttons.
        super().__init__(parent)
        self.controller = controller

        self.configure(style="TFrame")

        ttk.Label(self, text="Login", style="Title.TLabel").pack(pady=20)

        ttk.Label(self, text="Username", style="TLabel").pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        ttk.Label(self, text="Password", style="TLabel").pack()
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack()

        ttk.Button(self, text="Login", command=lambda: (play_sound(), self.login()), style="TButton").pack(pady=10)
        ttk.Button(self, text="Register", command=lambda: (play_sound(), controller.show_frame("Register")), style="TButton").pack()

    # Handles login logic: verifies credentials and navigates on success.
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = login_user(username, password)
        if success:
            self.controller.set_user(username)
            messagebox.showinfo("Success", message)
            self.controller.show_frame("MainMenu")
        else:
            messagebox.showerror("Error", message)

# Plays a click sound effect when triggered.
def play_sound():
    play_sound_effect("assets/sfx/click.wav")