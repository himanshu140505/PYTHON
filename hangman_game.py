import random
from tkinter import messagebox
from tkinter_app import TkinterApp

class HangmanGame:
    def __init__(self, app):
        self.app = app
        self.words = ["python", "java", "kotlin", "javascript"]
        self.word = random.choice(self.words)
        self.guessed_word = ["_"] * len(self.word)
        self.attempts = 6
        self.guessed_letters = set()

    def update_display(self):
        self.app.clear_text()
        self.app.insert_text(" ".join(self.guessed_word))
        self.app.insert_text(f"Attempts left: {self.attempts}")

    def guess_letter(self, event=None):
        guess = self.app.input_box.get().lower()
        self.app.input_box.delete(0, tk.END)

        if guess in self.guessed_letters:
            messagebox.showinfo("Hangman", "You already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess
        else:
            self.attempts -= 1
            messagebox.showinfo("Hangman", f"Wrong guess. You have {self.attempts} attempts left.")

        self.update_display()

        if "_" not in self.guessed_word:
            messagebox.showinfo("Hangman", f"Congratulations! You guessed the word: {self.word}")
            self.app.root.quit()
        elif self.attempts == 0:
            messagebox.showinfo("Hangman", f"Game over. The word was: {self.word}")

    def start(self):
        self.app.insert_text("Welcome to Hangman!")
        self.app.create_box(font=("Helvetica", 14))
        self.app.input_box.bind("<Return>", self.guess_letter)
        self.update_display()
        self.app.run()
        self.app.insert_text("Welcome to Hangman!")
if __name__ == "__main__":
    app = TkinterApp('Hangman Game')
    hangman_game = HangmanGame(app)
    hangman_game.start()