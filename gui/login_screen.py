import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from auth.auth import login_user

class LoginScreen(ttk.Frame):  # Inherit from ttk.Frame
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(style="TFrame")  # Apply frame style

        ttk.Label(self, text="Login", style="Title.TLabel").pack(pady=20)

        ttk.Label(self, text="Username", style="TLabel").pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        ttk.Label(self, text="Password", style="TLabel").pack()
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack()

        ttk.Button(self, text="Login", command=self.login, style="TButton").pack(pady=10)
        ttk.Button(self, text="Register", command=lambda: controller.show_frame("Register"), style="TButton").pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success, message = login_user(username, password)
        if success:
            self.controller.set_user(username)  # Store user in session
            messagebox.showinfo("Success", message)
            self.controller.show_frame("MainMenu")
        else:
            messagebox.showerror("Error", message)
