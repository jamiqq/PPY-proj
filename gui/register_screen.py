# gui/register_screen.py
import tkinter as tk
from tkinter import messagebox
from auth.auth import register_user

class RegisterScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Register", font=("Arial", 18)).pack(pady=20)

        tk.Label(self, text="New Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="New Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Create Account", command=self.register).pack(pady=10)
        tk.Button(self, text="Back to Login", command=lambda: controller.show_frame("Login")).pack()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = register_user(username, password)
        if success:
            messagebox.showinfo("Success", message)
            self.controller.show_frame("Login")
        else:
            messagebox.showerror("Error", message)
