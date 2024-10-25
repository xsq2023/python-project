import tkinter as tk
import random

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048游戏")
        self.grid_size = 4
        self.cell_size = 100
        self.board = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.create_widgets()
        self.new_number()
        self.update_board()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.cell_size * self.grid_size, height=self.cell_size * self.grid_size)
        self.canvas.pack()
        self.root.bind("<Key>", self.key_press)

    def new_number(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = random.choice([2, 4])

    def update_board(self):
        self.canvas.delete("all")
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.board[i][j]
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = self.get_color(value)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                if value:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(value), font=("Arial", 24))

    def get_color(self, value):
        colors = {
            0: "#CCCCCC", 2: "#FFE4B5", 4: "#FFD700", 8: "#FFA500", 
            16: "#FF4500", 32: "#FF0000", 64: "#DC143C", 128: "#C71585",
            256: "#DB7093", 512: "#FF1493", 1024: "#FF69B4", 2048: "#FFB6C1"
        }
        return colors.get(value, "#A9A9A9")

    def key_press(self, event):
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            if self.move(event.keysym):
                self.new_number()
                self.update_board()

    def move(self, direction):
        original_board = [row[:] for row in self.board]
        if direction == 'Left':
            for i in range(self.grid_size):
                self.board[i] = self.merge(self.board[i])
        elif direction == 'Right':
            for i in range(self.grid_size):
                self.board[i] = self.merge(self.board[i][::-1])[::-1]
        elif direction == 'Up':
            for j in range(self.grid_size):
                col = [self.board[i][j] for i in range(self.grid_size)]
                merged_col = self.merge(col)
                for i in range(self.grid_size):
                    self.board[i][j] = merged_col[i]
        elif direction == 'Down':
            for j in range(self.grid_size):
                col = [self.board[i][j] for i in range(self.grid_size)]
                merged_col = self.merge(col[::-1])[::-1]
                for i in range(self.grid_size):
                    self.board[i][j] = merged_col[i]
        return original_board != self.board  # 检查是否有移动

    def merge(self, line):
        new_line = [num for num in line if num != 0]
        for i in range(len(new_line) - 1):
            if new_line[i] == new_line[i + 1]:
                new_line[i] *= 2
                new_line[i + 1] = 0
        new_line = [num for num in new_line if num != 0]
        return new_line + [0] * (self.grid_size - len(new_line))


def start_game():
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()

if __name__ == "__main__":
    start_game()