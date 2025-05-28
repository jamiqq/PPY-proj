import tkinter as tk
from gui.styles import styles

class ScreenController(tk.Tk):
    def __init__(self):
        # Initializes the main application window and sets up base styles.
        super().__init__()
        styles.setup_styles()
        self.title("Hangman Game")
        self.geometry("800x600")
        self.resizable(False, False)
        self.frames = {}
        self.current_user = None

        # Configure the main layout to expand with window size
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # Adds a new screen frame to the controller and places it in the grid.
    def add_frame(self, name, frame_class):
        frame = frame_class(parent=self, controller=self)
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    # Displays the specified frame. Calls refresh method if available.
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if hasattr(frame, "refresh_stats"):
            frame.refresh_stats()
        frame.tkraise()

    # Sets the current logged-in user's username.
    def set_user(self, username):
        self.current_user = username

    # Returns the username of the current logged-in user.
    def get_user(self):
        return self.current_user
