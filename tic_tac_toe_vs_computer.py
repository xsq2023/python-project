import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [' '] * 9
        self.current_player = 'X'
        self.buttons = []
        self.create_buttons()
        
        self.score = {'X': 0, 'O': 0, 'Tie': 0}

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.master, text=' ', font='Arial 20', width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == ' ' and self.current_player == 'X':
            self.board[index] = 'X'
            self.buttons[index].config(text='X')
            if self.check_winner('X'):
                self.update_score('X')
            else:
                self.current_player = 'O'
                self.computer_move()

    def computer_move(self):
        vacant_places = [i for i in range(9) if self.board[i] == ' ']
        if vacant_places:
            index = random.choice(vacant_places)
            self.board[index] = 'O'
            self.buttons[index].config(text='O')
            if self.check_winner('O'):
                self.update_score('O')
            else:
                self.current_player = 'X'
    
    def check_winner(self, letter):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if all(self.board[i] == letter for i in combo):
                messagebox.showinfo("Game Over", f"{letter} wins!")
                self.reset_board()
                return True
        if ' ' not in self.board:
            messagebox.showinfo("Game Over", "It's a Tie!")
            self.score['Tie'] += 1
            self.reset_board()
            return True
        return False

    def update_score(self, letter):
        self.score[letter] += 1
        messagebox.showinfo("Score", f"X: {self.score['X']} O: {self.score['O']} Tie: {self.score['Tie']}")
        self.reset_board()

    def reset_board(self):
        self.board = [' '] * 9
        for button in self.buttons:
            button.config(text=' ')
        self.current_player = 'X'

def start_game():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    start_game()
