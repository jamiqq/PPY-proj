import tkinter as tk
from tkinter import messagebox

class PlaySelectionScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = tk.Label(self, text="Select Game Mode", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        btn_classic = tk.Button(self, text="Classic", width=20, command=self.play_classic)
        btn_classic.pack(pady=10)

        btn_custom = tk.Button(self, text="Custom Word", width=20, command=self.play_custom)
        btn_custom.pack(pady=10)

        btn_category = tk.Button(self, text="Category", width=20, command=self.play_category)
        btn_category.pack(pady=10)

        btn_back = tk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("MainMenu"))
        btn_back.pack(pady=20)

    def play_classic(self):
        messagebox.showinfo("Classic Mode", "Classic mode selected. (To be implemented)")

    def play_custom(self):
        popup = tk.Toplevel(self)
        popup.title("Enter Custom Word")
        popup.geometry("300x150")
        popup.resizable(False, False)
        popup.grab_set()  # Make modal (block interaction with main window)

        label = tk.Label(popup, text="Enter the secret word:", font=("Arial", 12))
        label.pack(pady=10)

        word_var = tk.StringVar()
        entry = tk.Entry(popup, textvariable=word_var, show="*")
        entry.pack(pady=5)
        entry.focus_set()

        def start_game():
            word = word_var.get().strip()
            if not word.isalpha():
                tk.messagebox.showerror("Invalid word", "Please enter a valid word (letters only).")
                return
            popup.destroy()

            popup.destroy()

            game_screen = self.controller.frames["GameScreen"]
            game_screen.set_word(word)

            self.controller.show_frame("GameScreen")

        def cancel():
            popup.destroy()

        btn_play = tk.Button(popup, text="Play", command=start_game)
        btn_play.pack(side="left", padx=20, pady=20)

        btn_back = tk.Button(popup, text="Back", command=cancel)
        btn_back.pack(side="right", padx=20, pady=20)
    def play_category(self):
        messagebox.showinfo("Category Mode", "Category mode selected. (To be implemented)")
