import random
import tkinter as tk
from tkinter import messagebox

def hangman():
    words = [
        "tiger", "superman", "thor", "doraemon", "avenger", "water", 
        "stream", "elephant", "giraffe", "python", "hangman", 
        "computer", "science", "programming", "developer", "keyboard", 
        "mouse", "monitor", "coffee", "chocolate", "piano", "guitar",
        "basketball", "soccer", "tennis", "badminton", "football", 
        "chicken", "pizza", "hamburger", "spaghetti", "sushi", 
        "apple", "banana", "orange", "grape", "watermelon", 
        "strawberry", "blueberry", "peach", "kiwi", "mango"
    ]
    
    return random.choice(words)

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.word = hangman()
        self.valid_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.turns = 10
        self.guess_made = ''
        
        self.master.title("Hangman Game")
        self.label = tk.Label(master, text="Guess the word: " + "_ " * len(self.word), font=("Courier", 14))
        self.label.pack(pady=20)
        
        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_guess)
        
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.turns_label = tk.Label(master, text=f"Turns left: {self.turns}")
        self.turns_label.pack(pady=5)

        self.hangman_frame = tk.Frame(master)
        self.hangman_frame.pack()

    def check_guess(self, event=None):
        guess = self.entry.get().casefold()
        self.entry.delete(0, tk.END)

        if guess in self.valid_letters and guess not in self.guess_made:
            self.guess_made += guess
            if guess not in self.word:
                self.turns -= 1
                self.update_hangman()
            self.update_display()
        else:
            messagebox.showinfo("Invalid Input", "Enter a valid letter or a letter you haven't guessed yet.")

        if self.turns == 0:
            messagebox.showinfo("Game Over", f"You lose! The word was: {self.word}")
            self.master.quit()

        if "_" not in self.update_display():
            messagebox.showinfo("Congratulations", "You win!")
            self.master.quit()

    def update_display(self):
        display_word = " ".join([letter if letter in self.guess_made else "_" for letter in self.word])
        self.label.config(text="Guess the word: " + display_word)
        return display_word

    def update_hangman(self):
        self.turns_label.config(text=f"Turns left: {self.turns}")
        if self.turns == 0:
            self.label.config(text=f"You let a kind man die! The word was: {self.word}")

def start_game():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()    



if __name__ == "__main__":
    start_game()
