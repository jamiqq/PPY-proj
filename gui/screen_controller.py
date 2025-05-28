# gui/screen_controller.py
import tkinter as tk
from gui.styles import styles


class ScreenController(tk.Tk):
    def __init__(self):
        super().__init__()
        styles.setup_styles()
        self.title("Hangman Game")
        self.geometry("800x600")
        self.resizable(False, False)
        self.frames = {}
        self.current_user = None  # <- Track current user

        # Allow row and column to expand and fill the space
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def add_frame(self, name, frame_class):
        frame = frame_class(parent=self, controller=self)
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if hasattr(frame, "refresh_stats"):
            frame.refresh_stats()
        frame.tkraise()

    def set_user(self, username):
        self.current_user = username

    def get_user(self):
        return self.current_user
