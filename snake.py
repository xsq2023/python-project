import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("贪吃蛇游戏")
        self.canvas_width = 400
        self.canvas_height = 400
        self.cell_size = 20
        self.snake = [(2, 2), (2, 1), (2, 0)]
        self.direction = "Down"
        self.food = None
        self.score = 0
        self.create_widgets()
        self.place_food()
        self.update_game()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()
        self.root.bind("<Key>", self.change_direction)

    def place_food(self):
        while True:
            x = random.randint(0, (self.canvas_width // self.cell_size) - 1)
            y = random.randint(0, (self.canvas_height // self.cell_size) - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def update_game(self):
        self.move_snake()
        if self.check_collision():
            self.game_over()
        else:
            self.draw()
            self.root.after(100, self.update_game)

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        else:  # Right
            new_head = (head_x + 1, head_y)

        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.score += 1
            self.place_food()
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()

    def check_collision(self):
        head_x, head_y = self.snake[0]
        return (head_x < 0 or head_x >= self.canvas_width // self.cell_size or
                head_y < 0 or head_y >= self.canvas_height // self.cell_size or
                self.snake[0] in self.snake[1:])

    def game_over(self):
        self.canvas.create_text(self.canvas_width // 2, self.canvas_height // 2,
                                 text="游戏结束", fill="white", font=("Arial", 24))
        self.root.update()

    def draw(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size,
                                          (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                                          fill="green")
        food_x, food_y = self.food
        self.canvas.create_oval(food_x * self.cell_size, food_y * self.cell_size,
                                (food_x + 1) * self.cell_size, (food_y + 1) * self.cell_size,
                                fill="red")

def start_game():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    start_game()