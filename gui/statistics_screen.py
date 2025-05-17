import tkinter as tk

class StatisticsScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = tk.Label(self, text="Player Statistics", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        self.stats_label = tk.Label(self, text="", font=("Arial", 14))
        self.stats_label.pack(pady=10)

        back_button = tk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("MainMenu"))
        back_button.pack(pady=20)

    def refresh_stats(self):
        user = self.controller.current_user
        # For now, we use mock stats. Later this pulls from DB
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
