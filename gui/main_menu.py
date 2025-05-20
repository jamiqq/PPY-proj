# gui/main_menu.py
import tkinter as tk
from tkinter import messagebox, filedialog


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="Main Menu", font=("Arial", 20))
        self.label.pack(pady=20)

        tk.Button(self, text="Play", width=20, command=self.play).pack(pady=5)
        tk.Button(self, text="Statistics", width=20, command=self.stats ).pack(pady=5)
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
        self.controller.show_frame("PlaySelectionScreen")

    def stats(self):
        self.controller.show_frame("StatisticsScreen")

    def add_category(self):
        # Open file dialog to select a file
        file_path = filedialog.askopenfilename(
            title="Select a Category File",
            filetypes=[("Text Files", "*.txt")]
        )
        if not file_path:
            # User cancelled
            return

        # Check if selected file is a .txt file
        if not file_path.lower().endswith('.txt'):
            messagebox.showerror("Invalid File", "Please select a valid .txt file.")
            return

        # Success feedback (actual parsing will be later)
        messagebox.showinfo("File Selected", f"Selected category file:\n{file_path}")

    def switch_user(self):
        self.controller.set_user(None)
        self.controller.show_frame("Login")

