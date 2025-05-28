from tkinter import ttk

from gui.styles.sound_manager import play_sound_effect
from db_handling.user_db import get_user_stats

class StatisticsScreen(ttk.Frame):
    def __init__(self, parent, controller):
        # Initializes the statistics screen UI elements.
        super().__init__(parent)
        self.controller = controller

        self.configure(style="TFrame")

        title = ttk.Label(self, text="Player Statistics", style="Title.TLabel")
        title.pack(pady=20)

        self.stats_label = ttk.Label(self, text="", style="TLabel", justify="left", anchor="w")
        self.stats_label.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Menu", command=lambda: (play_sound(), controller.show_frame("MainMenu")), style="TButton")
        back_button.pack(pady=20)

    # Retrieves and displays statistics for the currently logged-in user.
    def refresh_stats(self):
        username = self.controller.get_user()
        stats = get_user_stats(username)

        if stats:
            stats_text = (
                f"Username: {username}\n\n"
                f"Games Played: {stats['games_played']}\n"
                f"Games Won: {stats['games_won']}\n"
                f"Games Lost: {stats['games_lost']}\n"
                f"Win Rate: {stats['win_rate']}%"
            )
        else:
            stats_text = "No statistics available for this user."

        self.stats_label.config(text=stats_text)

# Plays a click sound effect when triggered.
def play_sound():
    play_sound_effect("assets/sfx/click.wav")
