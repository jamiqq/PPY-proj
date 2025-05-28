# main.py
from gui.category_word_uploader import CategoryWordUploader
from gui.classic_mode import ClassicGameSetupScreen
from gui.screen_controller import ScreenController
from gui.login_screen import LoginScreen
from gui.register_screen import RegisterScreen
from gui.main_menu import MainMenu
from gui.statistics_screen import StatisticsScreen
from gui.play_selection_screen import PlaySelectionScreen
from gui.game_screen import GameScreen
from gui.styles.sound_manager import play_background_music

# Initializes and starts the application with all GUI frames.
def start_app():
    app = ScreenController()
    app.add_frame("Login", LoginScreen)
    app.add_frame("Register", RegisterScreen)
    app.add_frame("MainMenu", MainMenu)
    app.add_frame("AddCategoryScreen", CategoryWordUploader)
    app.add_frame("StatisticsScreen", StatisticsScreen)
    app.add_frame("PlaySelectionScreen", PlaySelectionScreen)
    app.add_frame("GameScreen", GameScreen)
    app.add_frame("ClassicGameSetupScreen", ClassicGameSetupScreen)

    app.show_frame("Login")
    app.mainloop()

# Entry point of the application; starts background music and launches the GUI.
if __name__ == "__main__":
    play_background_music("assets/music/theme.mp3")
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
