import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from gui.styles.sound_manager import play_sound_effect


class PlaySelectionScreen(ttk.Frame):  # inherit from ttk.Frame
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(style="TFrame")

        title = ttk.Label(self, text="Select Game Mode", style="Title.TLabel")
        title.pack(pady=20)

        btn_classic = ttk.Button(self, text="Classic", width=20, command=lambda: (play_sound(), self.play_classic()), style="TButton")
        btn_classic.pack(pady=10)

        btn_custom = ttk.Button(self, text="Custom Word", width=20, command=lambda: (play_sound(), self.play_custom()), style="TButton")
        btn_custom.pack(pady=10)

        btn_category = ttk.Button(self, text="Category", width=20, command=lambda: (play_sound(), self.play_category()), style="TButton")
        btn_category.pack(pady=10)

        btn_back = ttk.Button(self, text="Back to Menu", command=lambda: (play_sound(), controller.show_frame("MainMenu")), style="TButton")
        btn_back.pack(pady=20)

    def play_classic(self):
        self.controller.show_frame("ClassicGameSetupScreen")

    def play_custom(self):
        popup = tk.Toplevel(self)
        popup.title("Enter Custom Word")
        popup.geometry("400x250")
        popup.resizable(True, True)
        popup.grab_set()  # Make modal

        label = ttk.Label(popup, text="Enter the secret word:", style="TLabel")
        label.pack(pady=10)

        word_var = tk.StringVar()
        entry = ttk.Entry(popup, textvariable=word_var, show="*")
        entry.pack(pady=5)
        entry.focus_set()

        def start_game():
            word = word_var.get().strip()
            if not word.isalpha():
                messagebox.showerror("Invalid word", "Please enter a valid word (letters only).")
                return
            popup.destroy()

            game_screen = self.controller.frames["GameScreen"]
            game_screen.set_word(word)

            self.controller.show_frame("GameScreen")

        def cancel():
            popup.destroy()

        btn_play = ttk.Button(popup, text="Play", command=lambda: (play_sound(), start_game()), style="TButton")
        btn_play.pack(side="left", padx=20, pady=20)

        btn_back = ttk.Button(popup, text="Back", command=lambda: (play_sound(), cancel()), style="TButton")
        btn_back.pack(side="right", padx=20, pady=20)

    def play_category(self):
        messagebox.showinfo("Category Mode", "Category mode selected. (To be implemented)")

def play_sound():
    play_sound_effect("assets/sfx/click.wav")