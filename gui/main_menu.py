from tkinter import messagebox, filedialog
from tkinter import ttk
from gui.styles import styles
from gui.styles.sound_manager import play_sound_effect


class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        # Initializes the main menu screen with navigation buttons and user display.
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

    # Updates and raises the frame, showing the currently logged-in user.
    def tkraise(self, *args, **kwargs):
        username = self.controller.get_user()
        self.user_label.config(text=f"Logged in as: {username}")
        super().tkraise(*args, **kwargs)

    # Navigates to the game mode selection screen.
    def play(self):
        self.controller.show_frame("PlaySelectionScreen")

    # Navigates to the statistics screen.
    def stats(self):
        self.controller.show_frame("StatisticsScreen")

    # Navigates to the add category screen.
    def add_category(self):
        self.controller.show_frame("AddCategoryScreen")

    # Logs out the user and returns to the login screen.
    def switch_user(self):
        self.controller.set_user(None)
        self.controller.show_frame("Login")

# Plays a click sound effect when triggered.
def play_sound():
    play_sound_effect("assets/sfx/click.wav")