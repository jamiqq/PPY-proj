# gui/main_menu.py
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from gui.styles import styles
from gui.styles.sound_manager import play_sound_effect


class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(style="TFrame")

        self.label = ttk.Label(self, text="Main Menu", font=styles.FONT_TITLE, foreground=styles.TEXT_COLOR)
        self.label.pack(pady=20)

        btn_play = ttk.Button(self, text="Play", width=20, command=lambda: (play_sound(), self.play()))
        btn_play.pack(pady=5)

        btn_stats = ttk.Button(self, text="Statistics", width=20, command=lambda: (play_sound(), self.stats()))
        btn_stats.pack(pady=5)

        btn_add_cat = ttk.Button(self, text="Add Category", width=20, command=lambda: (play_sound(), self.add_category()))
        btn_add_cat.pack(pady=5)

        btn_switch = ttk.Button(self, text="Switch User", width=20, command=lambda: (play_sound(), self.switch_user()))
        btn_switch.pack(pady=5)

        btn_exit = ttk.Button(self, text="Exit", width=20, command=lambda: (play_sound(), self.controller.quit()))
        btn_exit.pack(pady=5)

        self.user_label = ttk.Label(self, text="", foreground="gray")
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

def play_sound():
    play_sound_effect("assets/sfx/click.wav")