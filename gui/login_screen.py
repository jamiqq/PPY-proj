# gui/login_screen.py
import tkinter as tk
from tkinter import messagebox
from auth.auth import login_user

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Login", font=("Arial", 18)).pack(pady=20)

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=10)
        tk.Button(self, text="Register", command=lambda: controller.show_frame("Register")).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = login_user(username, password)
        if success:
            self.controller.set_user(username)  # <- Store user in session
            messagebox.showinfo("Success", message)
            self.controller.show_frame("MainMenu")
        else:
            messagebox.showerror("Error", message)
