import random
import operator
from random import sample
import tkinter as tk
from tkinter import messagebox

# 生成数独棋盘
def generate_board(num):
    base = 3
    side = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    def shuffle(s):
        return sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    board_tmp = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * 3 // 4 if num == 0 else 81 - num
    for p in sample(range(squares), empties):
        board_tmp[p // side][p % side] = 0

    return board_tmp

def possible(bo, pos, num):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

def next_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j 

def get_hint(bo):
    slot = next_empty(bo)
    if not slot:
        return None
    row, col = slot
    hints = []
    for num in range(1, 10):
        if possible(bo, (row, col), num):
            hints.append(num)
    return hints

def solve(bo):
    slot = next_empty(bo)
    if not slot:
        return True
    else:
        row, col = slot
    for i in range(1, 10):
        if possible(bo, (row, col), i):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False

class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("数独游戏")
        self.board = generate_board(0)
        self.solution = [row[:] for row in self.board]
        solve(self.solution)  # 求解并保存答案
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        self.create_widgets()
        self.display_board()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.master, width=3, font=('Arial', 18), justify='center', bd=2)
                entry.grid(row=i, column=j, padx=5, pady=5)
                
                # 每个3x3大格子添加边框
                if i % 3 == 0 and j % 3 == 0:
                    entry.config(bd=5, relief='ridge')

                self.entries[i][j] = entry

        self.submit_button = tk.Button(self.master, text="提交", command=self.submit_answer)
        self.submit_button.grid(row=10, column=0, columnspan=3, pady=10)

        self.hint_button = tk.Button(self.master, text="获取提示", command=self.get_hint)
        self.hint_button.grid(row=10, column=3, columnspan=3, pady=10)

        self.show_solution_button = tk.Button(self.master, text="显示答案", command=self.show_solution)
        self.show_solution_button.grid(row=11, column=0, columnspan=6, pady=10)

    def display_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.board[i][j]))
                    self.entries[i][j].config(state='readonly')  # 只读模式

    def submit_answer(self):
        for i in range(9):
            for j in range(9):
                if self.entries[i][j].get() != "":
                    try:
                        num = int(self.entries[i][j].get())
                        if not possible(self.board, (i, j), num):
                            messagebox.showerror("错误", f"数字 {num} 在位置 ({i}, {j}) 不合法。")
                            return
                        self.board[i][j] = num
                    except ValueError:
                        messagebox.showerror("错误", "请输入有效的数字 (1-9)。")
                        return

        if not next_empty(self.board):
            messagebox.showinfo("完成", "恭喜你，完成了数独！")

    def get_hint(self):
        hints = get_hint(self.board)
        if hints:
            slot = next_empty(self.board)
            if slot:
                row, col = slot
                messagebox.showinfo("提示", f"在位置 ({row}, {col}) 可填的数字: {hints}")
        else:
            messagebox.showinfo("提示", "没有可用的提示。")

    def show_solution(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state='normal')  # 允许编辑
                self.entries[i][j].delete(0, tk.END)  # 清空当前输入
                if self.solution[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.solution[i][j]))  # 显示答案
                self.entries[i][j].config(state='readonly')  # 重新设为只读

def start_game():
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()    


if __name__ == "__main__":
    start_game()
