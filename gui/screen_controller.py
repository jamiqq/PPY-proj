# gui/screen_controller.py
import tkinter as tk
from gui.statistics_screen import StatisticsScreen

class ScreenController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangman Game")
        self.geometry("600x400")
        self.resizable(False, False)
        self.frames = {}
        self.current_user = None  # <- Track current user

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
