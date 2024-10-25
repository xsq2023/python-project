import tkinter as tk
import random
import math

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("贪吃蛇游戏")
        self.canvas_width = 400
        self.canvas_height = 400
        self.cell_size = 20
        self.snake = [(2, 2), (2, 1), (2, 0)]
        self.direction = "Right"  # 初始方向
        self.food = None
        self.score = 0
        self.create_widgets()
        
        # 初始化已访问位置集合
        self.visited_positions = set(tuple(x) for x in self.snake)
        
        # 放置食物，确保不在蛇身上且远离蛇头
        self.place_food()
        
        # 开始游戏循环
        self.update_game()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()
        self.root.bind("<Key>", self.change_direction)

    def place_food(self):
        min_distance = 15 # 设置新食物与蛇头之间的最小距离，单位为格子数量
        while True:
            x = random.randint(0, (self.canvas_width // self.cell_size) - 1)
            y = random.randint(0, (self.canvas_height // self.cell_size) - 1)
            new_food = (x, y)
            
            # 计算新食物与蛇头之间的距离
            head_x, head_y = self.snake[0]
            distance = math.sqrt((head_x - x) ** 2 + (head_y - y) ** 2)
            
            # 确保新食物不在蛇身上，且与蛇头保持一定距离
            if new_food not in self.snake and new_food not in self.visited_positions and distance >= min_distance:
                self.food = new_food
                self.visited_positions.add(new_food)
                break

    def update_game(self):
        self.ai_move()
        if self.move_snake():
            self.draw()
            self.root.after(100, self.update_game)
        else:
            self.game_over()

    def ai_move(self):
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food
        possible_directions = ["Up", "Down", "Left", "Right"]
        best_direction = None

        # 优先选择朝向食物的方向
        if head_x > food_x and "Left" not in self.get_blocked_directions():
            best_direction = "Left"
        elif head_x < food_x and "Right" not in self.get_blocked_directions():
            best_direction = "Right"
        elif head_y > food_y and "Up" not in self.get_blocked_directions():
            best_direction = "Up"
        elif head_y < food_y and "Down" not in self.get_blocked_directions():
            best_direction = "Down"

        # 如果没有直接朝向食物的方向，选择一个不撞墙的方向
        if best_direction is None:
            possible_directions = [d for d in possible_directions if d not in self.get_blocked_directions()]
            if possible_directions:
                best_direction = possible_directions[0]

        # 确保蛇不会直接向相反方向移动
        opposite_direction = self.get_opposite_direction(self.direction)
        if best_direction == opposite_direction:
            possible_directions.remove(opposite_direction)
            if possible_directions:
                best_direction = possible_directions[0]

        self.direction = best_direction

    def get_blocked_directions(self):
        head_x, head_y = self.snake[0]
        blocked = []
        if head_x == 0 or (head_x - 1, head_y) in self.snake:
            blocked.append("Left")
        if head_x == self.canvas_width // self.cell_size - 1 or (head_x + 1, head_y) in self.snake:
            blocked.append("Right")
        if head_y == 0 or (head_x, head_y - 1) in self.snake:
            blocked.append("Up")
        if head_y == self.canvas_height // self.cell_size - 1 or (head_x, head_y + 1) in self.snake:
            blocked.append("Down")
        return blocked

    def get_new_head(self, direction):
        head_x, head_y = self.snake[0]
        if direction == "Up":
            return (head_x, head_y - 1)
        elif direction == "Down":
            return (head_x, head_y + 1)
        elif direction == "Left":
            return (head_x - 1, head_y)
        elif direction == "Right":
            return (head_x + 1, head_y)

    def is_collision(self, new_head):
        head_x, head_y = new_head
        return (head_x < 0 or head_x >= self.canvas_width // self.cell_size or
                head_y < 0 or head_y >= self.canvas_height // self.cell_size or
                new_head in self.snake)

    def change_direction(self, event):
        new_direction = event.keysym
        if new_direction in ["Up", "Down", "Left", "Right"] and new_direction != self.get_opposite_direction(self.direction):
            self.direction = new_direction

    def get_opposite_direction(self, direction):
        opposites = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
        return opposites[direction]

    def move_snake(self):
        head_x, head_y = self.snake[0]
        new_head = self.get_new_head(self.direction)

        if self.is_collision(new_head):
            return False

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

        return True

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

def start_game_snake():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    start_game_snake()
