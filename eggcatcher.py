from itertools import cycle
from random import randrange
import tkinter as tk
from tkinter import messagebox

class EggCatcherGame:
    def __init__(self, master):
        self.master = master
        self.canvas_width = 800
        self.canvas_height = 400
        self.c = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, background='deep sky blue')
        self.c.create_rectangle(-5, self.canvas_height - 100, self.canvas_width + 5, self.canvas_height + 5, fill='sea green', width=0)
        self.c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
        self.c.pack()

        # Game design variables
        self.color_cycle = cycle(['light blue', 'light pink', 'light yellow', 'light green', 'red', 'blue', 'green', 'black'])
        self.egg_width = 45
        self.egg_height = 55
        self.egg_score = 10
        self.egg_speed = 500
        self.egg_interval = 4000
        self.difficulty_factor = 0.95

        # Catcher setup
        self.catcher_color = 'blue'
        self.catcher_width = 100
        self.catcher_height = 100
        self.catcher_start_x = self.canvas_width / 2 - self.catcher_width / 2
        self.catcher_start_y = self.canvas_height - self.catcher_height - 20
        self.catcher_start_x2 = self.catcher_start_x + self.catcher_width
        self.catcher_start_y2 = self.catcher_start_y + self.catcher_height

        self.catcher = self.c.create_arc(self.catcher_start_x, self.catcher_start_y, self.catcher_start_x2, self.catcher_start_y2, start=200, extent=140, style='arc', outline=self.catcher_color, width=3)

        # Score and lives setup
        self.score = 0
        self.score_text = self.c.create_text(10, 10, anchor='nw', font=('Arial', 18, 'bold'), fill='darkblue', text='Score : ' + str(self.score))

        self.lives_remaining = 3
        self.lives_text = self.c.create_text(self.canvas_width - 10, 10, anchor='ne', font=('Arial', 18, 'bold'), fill='darkblue', text='Lives : ' + str(self.lives_remaining))

        self.eggs = []

        # Event handlers for moving the catcher
        self.c.bind('<Left>', self.move_left)
        self.c.bind('<Right>', self.move_right)
        self.c.focus_set()

    def start_game(self):
        self.master.after(1000, self.create_eggs)
        self.master.after(1000, self.move_eggs)
        self.master.after(1000, self.catch_check)

    # Function to create eggs at random positions
    def create_eggs(self):
        x = randrange(10, 740)
        y = 40
        new_egg = self.c.create_oval(x, y, x + self.egg_width, y + self.egg_height, fill=next(self.color_cycle), width=0)
        self.eggs.append(new_egg)
        self.master.after(self.egg_interval, self.create_eggs)

    # Function to move eggs downwards
    def move_eggs(self):
        for egg in self.eggs:
            (egg_x, egg_y, egg_x2, egg_y2) = self.c.coords(egg)
            self.c.move(egg, 0, 10)
            if egg_y2 > self.canvas_height:
                self.egg_dropped(egg)
        self.master.after(self.egg_speed, self.move_eggs)

    # Function to handle egg drop events
    def egg_dropped(self, egg):
        self.eggs.remove(egg)
        self.c.delete(egg)
        self.lose_a_life()
        if self.lives_remaining == 0:
            response = messagebox.askyesno('GAME OVER!', 'Final Score: ' + str(self.score) + '\nDo you want to play again?')
            if response:
                self.reset_game()
            else:
                self.master.quit()

    # Function to reset the game state for a new game
    def reset_game(self):
        for egg in self.eggs:
            self.c.delete(egg)
        self.eggs = []
        self.score = 0
        self.lives_remaining = 3
        self.c.itemconfigure(self.score_text, text='Score : ' + str(self.score))
        self.c.itemconfigure(self.lives_text, text='Lives : ' + str(self.lives_remaining))
        self.master.after(1000, self.create_eggs)
        self.master.after(1000, self.move_eggs)
        self.master.after(1000, self.catch_check)

    # Function to decrease lives
    def lose_a_life(self):
        self.lives_remaining -= 1
        self.c.itemconfigure(self.lives_text, text='Lives : ' + str(self.lives_remaining))

    # Function to check if eggs are caught
    def catch_check(self):
        (catcher_x, catcher_y, catcher_x2, catcher_y2) = self.c.coords(self.catcher)
        for egg in self.eggs:
            (egg_x, egg_y, egg_x2, egg_y2) = self.c.coords(egg)
            if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
                self.eggs.remove(egg)
                self.c.delete(egg)
                self.increase_score(self.egg_score)
        self.master.after(100, self.catch_check)

    # Function to increase the score
    def increase_score(self, points):
        self.score += points
        self.egg_speed = int(self.egg_speed * self.difficulty_factor)
        self.egg_interval = int(self.egg_interval * self.difficulty_factor)
        self.c.itemconfigure(self.score_text, text='Score : ' + str(self.score))

    # Event handlers for moving the catcher
    def move_left(self, event):
        (x1, y1, x2, y2) = self.c.coords(self.catcher)
        if x1 > 0:
            self.c.move(self.catcher, -20, 0)

    def move_right(self, event):
        (x1, y1, x2, y2) = self.c.coords(self.catcher)
        if x2 < self.canvas_width:
            self.c.move(self.catcher, 20, 0)


# 入口函数，用于启动游戏
def start_egg_catcher_game():
    root = tk.Tk()
    game = EggCatcherGame(root)
    game.start_game()
    root.mainloop()

if __name__ == "__main__":
    start_egg_catcher_game()