# main.py
from gui.classic_mode import ClassicGameSetupScreen
from gui.screen_controller import ScreenController
from gui.login_screen import LoginScreen
from gui.register_screen import RegisterScreen
from gui.main_menu import MainMenu
from gui.statistics_screen import StatisticsScreen
from gui.play_selection_screen import PlaySelectionScreen
from gui.game_screen import GameScreen

def start_app():
    app = ScreenController()
    app.add_frame("Login", LoginScreen)
    app.add_frame("Register", RegisterScreen)
    app.add_frame("MainMenu", MainMenu)
    app.add_frame("StatisticsScreen", StatisticsScreen)
    app.add_frame("PlaySelectionScreen", PlaySelectionScreen)
    app.add_frame("GameScreen", GameScreen)
    app.add_frame("ClassicGameSetupScreen", ClassicGameSetupScreen)
    # Add other screens similarly

    app.show_frame("Login")
    app.mainloop()

if __name__ == "__main__":
    start_app()

# App Start
# └── Login/Register Screen (required)
#     └── Main Menu (after login)
#         ├── Play
#         │   └── Game Mode Selection
#         │       ├── Classic Mode
#         │       └── Own Word Mode
#         ├── Statistics
#         ├── Add Category
#         └── Exit
