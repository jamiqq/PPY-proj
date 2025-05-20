import tkinter as tk
from tkinter import messagebox

class GameScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.secret_word = ""
        self.guessed_letters = set()
        self.max_tries = 6
        self.tries_left = self.max_tries

        # Title
        self.title_label = tk.Label(self, text="Hangman Game", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        # Hangman canvas (placeholder for drawing)
        self.hangman_canvas = tk.Canvas(self, width=200, height=200, bg="white")
        self.hangman_canvas.pack(pady=10)

        # Word display (masked word with underscores)
        self.word_var = tk.StringVar(value="Word: ")
        self.word_label = tk.Label(self, textvariable=self.word_var, font=("Arial", 16))
        self.word_label.pack(pady=10)

        # Entry for guessing letters
        self.guess_var = tk.StringVar()
        self.guess_entry = tk.Entry(self, textvariable=self.guess_var, width=5, font=("Arial", 16))
        self.guess_entry.pack(pady=5)
        self.guess_entry.focus_set()

        # Guess button
        self.guess_button = tk.Button(self, text="Guess", command=self.guess_letter)
        self.guess_button.pack(pady=5)

        # Feedback message label
        self.feedback_var = tk.StringVar()
        self.feedback_label = tk.Label(self, textvariable=self.feedback_var, font=("Arial", 14))
        self.feedback_label.pack(pady=10)

        # Tries left label
        self.tries_var = tk.StringVar(value=f"Tries left: {self.tries_left}")
        self.tries_label = tk.Label(self, textvariable=self.tries_var, font=("Arial", 14))
        self.tries_label.pack(pady=5)

        # Back button
        self.back_button = tk.Button(self, text="Back to Menu", command=self.back_to_menu)
        self.back_button.pack(pady=10)

    def set_word(self, word):
        self.secret_word = word.lower()
        self.guessed_letters = set()
        self.tries_left = self.max_tries
        self.update_word_display()
        self.feedback_var.set("")
        self.tries_var.set(f"Tries left: {self.tries_left}")
        self.clear_hangman()
        self.guess_entry.focus_set()

    def update_word_display(self):
        displayed = [letter if letter in self.guessed_letters else "_" for letter in self.secret_word]
        self.word_var.set("Word: " + " ".join(displayed))

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

    def end_game(self, won):
        if won:
            messagebox.showinfo("Game Over", f"Congratulations! You guessed the word: {self.secret_word}")
        else:
            messagebox.showinfo("Game Over", f"You lost! The word was: {self.secret_word}")
        self.back_to_menu()

    def back_to_menu(self):
        self.controller.show_frame("MainMenu")

    def clear_hangman(self):
        self.hangman_canvas.delete("all")

    def draw_hangman(self):
        # Simple stick figure drawing progressing by tries lost
        self.clear_hangman()
        tries_used = self.max_tries - self.tries_left

        # Base
        if tries_used >= 1:
            self.hangman_canvas.create_line(20, 180, 180, 180, width=2)  # ground
        # Pole
        if tries_used >= 2:
            self.hangman_canvas.create_line(50, 180, 50, 20, width=2)
        # Beam
        if tries_used >= 3:
            self.hangman_canvas.create_line(50, 20, 120, 20, width=2)
        # Rope
        if tries_used >= 4:
            self.hangman_canvas.create_line(120, 20, 120, 40, width=2)
        # Head
        if tries_used >= 5:
            self.hangman_canvas.create_oval(100, 40, 140, 80, width=2)
        # Body
        if tries_used >= 6:
            self.hangman_canvas.create_line(120, 80, 120, 130, width=2)
            self.hangman_canvas.create_line(120, 90, 90, 110, width=2)  # left arm
            self.hangman_canvas.create_line(120, 90, 150, 110, width=2)  # right arm
            self.hangman_canvas.create_line(120, 130, 90, 160, width=2)  # left leg
            self.hangman_canvas.create_line(120, 130, 150, 160, width=2)  # right leg
