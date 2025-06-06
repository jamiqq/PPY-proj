import tkinter as tk
from tkinter import ttk, messagebox

from db_handling.user_db import update_user_stats
from gui.styles.sound_manager import play_sound_effect


class GameScreen(ttk.Frame):
    def __init__(self, parent, controller):
        # Initialize the game screen UI components and variables.
        super().__init__(parent, style="TFrame")
        self.controller = controller

        self.secret_word = ""
        self.guessed_letters = set()
        self.max_tries = 6
        self.tries_left = self.max_tries

        # Title
        self.title_label = ttk.Label(self, text="Hangman Game", style="Title.TLabel")
        self.title_label.pack(pady=10)

        # Hangman canvas
        self.hangman_canvas = tk.Canvas(self, width=200, height=200, bg="white", highlightthickness=1, highlightbackground="#ccc")
        self.hangman_canvas.pack(pady=10)

        # Word display (masked word with underscores)
        self.word_var = tk.StringVar(value="Word: ")
        self.word_label = ttk.Label(self, textvariable=self.word_var, style="TLabel", font=("Arial", 16))
        self.word_label.pack(pady=10)

        # Entry for guessing letters
        self.guess_var = tk.StringVar()
        self.guess_entry = ttk.Entry(self, textvariable=self.guess_var, width=5, font=("Arial", 16))
        self.guess_entry.pack(pady=5)
        self.guess_entry.focus_set()

        # Guess button
        self.guess_button = ttk.Button(self, text="Guess", command=lambda: (play_sound(), self.guess_letter()), style="TButton")
        self.guess_button.pack(pady=5)

        # Feedback message label
        self.feedback_var = tk.StringVar()
        self.feedback_label = ttk.Label(self, textvariable=self.feedback_var, style="TLabel", font=("Arial", 14))
        self.feedback_label.pack(pady=10)

        # Tries left label
        self.tries_var = tk.StringVar(value=f"Tries left: {self.tries_left}")
        self.tries_label = ttk.Label(self, textvariable=self.tries_var, style="TLabel", font=("Arial", 14))
        self.tries_label.pack(pady=5)

        # Back button
        self.back_button = ttk.Button(self, text="Back to Menu", command=lambda: (play_sound(), self.back_to_menu()), style="TButton")
        self.back_button.pack(pady=10)

    # Sets a new secret word and resets the game state.
    def set_word(self, word):
        self.secret_word = word.lower()
        self.guessed_letters = set()
        self.tries_left = self.max_tries
        self.update_word_display()
        self.feedback_var.set("")
        self.tries_var.set(f"Tries left: {self.tries_left}")
        self.clear_hangman()
        self.guess_entry.focus_set()

    # Updates the displayed word with guessed letters and underscores.
    def update_word_display(self):
        displayed = [letter if letter in self.guessed_letters else "_" for letter in self.secret_word]
        self.word_var.set("Word: " + " ".join(displayed))

    # Processes the player's guessed letter and updates the game state.
    def guess_letter(self):
        letter = self.guess_var.get().strip().lower()
        self.guess_var.set("")

        if len(letter) != 1 or not letter.isalpha():
            self.feedback_var.set("Please enter a single letter.")
            return

        if letter in self.guessed_letters:
            self.feedback_var.set(f"You already guessed '{letter}'. Try another letter.")
            return

        self.guessed_letters.add(letter)

        if letter in self.secret_word:
            self.feedback_var.set(f"Good guess! '{letter}' is in the word.")
            self.update_word_display()
            if all(l in self.guessed_letters for l in self.secret_word):
                self.end_game(won=True)
        else:
            self.tries_left -= 1
            self.tries_var.set(f"Tries left: {self.tries_left}")
            self.feedback_var.set(f"Sorry, '{letter}' is not in the word.")
            self.draw_hangman()
            if self.tries_left == 0:
                self.end_game(won=False)

    # Ends the game, updates user stats, shows message, and returns to menu.
    def end_game(self, won):
        user = self.controller.get_user()
        if user:
            update_user_stats(user, won=won)
        if won:
            messagebox.showinfo("Game Over", f"Congratulations! You guessed the word: {self.secret_word}")
        else:
            messagebox.showinfo("Game Over", f"You lost! The word was: {self.secret_word}")
        self.back_to_menu()

    # Returns to the main menu screen.
    def back_to_menu(self):
        self.controller.show_frame("MainMenu")

    # Clears the hangman drawing from the canvas.
    def clear_hangman(self):
        self.hangman_canvas.delete("all")

    # Draws hangman figure progressively as tries are used.
    def draw_hangman(self):
        self.clear_hangman()
        tries_used = self.max_tries - self.tries_left

        # Draw hangman steps
        if tries_used >= 1:
            self.hangman_canvas.create_line(20, 180, 180, 180, width=2)  # ground
        if tries_used >= 2:
            self.hangman_canvas.create_line(50, 180, 50, 20, width=2)    # pole
        if tries_used >= 3:
            self.hangman_canvas.create_line(50, 20, 120, 20, width=2)    # beam
        if tries_used >= 4:
            self.hangman_canvas.create_line(120, 20, 120, 40, width=2)   # rope
        if tries_used >= 5:
            self.hangman_canvas.create_oval(100, 40, 140, 80, width=2)   # head
        if tries_used >= 6:
            self.hangman_canvas.create_line(120, 80, 120, 130, width=2)  # body
            self.hangman_canvas.create_line(120, 90, 90, 110, width=2)   # left arm
            self.hangman_canvas.create_line(120, 90, 150, 110, width=2)  # right arm
            self.hangman_canvas.create_line(120, 130, 90, 160, width=2)  # left leg
            self.hangman_canvas.create_line(120, 130, 150, 160, width=2) # right leg


# Plays a click sound effect when triggered.
def play_sound():
    play_sound_effect("assets/sfx/click.wav")