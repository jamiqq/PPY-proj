import tkinter as tk
from tkinter import ttk

from gui.styles.sound_manager import play_sound_effect


class StatisticsScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(style="TFrame")

        title = ttk.Label(self, text="Player Statistics", style="Title.TLabel")
        title.pack(pady=20)

        self.stats_label = ttk.Label(self, text="", style="TLabel", justify="left", anchor="w")
        self.stats_label.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Menu", command=lambda: (play_sound(), controller.show_frame("MainMenu")), style="TButton")
        back_button.pack(pady=20)

    def refresh_stats(self):
        user = self.controller.current_user
        mock_stats = {
            "games_played": 12,
            "games_won": 7,
            "games_lost": 5
        }
        stats_text = (
            f"Username: {user}\n\n"
            f"Games Played: {mock_stats['games_played']}\n"
            f"Games Won: {mock_stats['games_won']}\n"
            f"Games Lost: {mock_stats['games_lost']}"
        )
        self.stats_label.config(text=stats_text)


def play_sound():
    play_sound_effect("assets/sfx/click.wav")