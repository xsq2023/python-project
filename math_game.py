import random
import operator
import tkinter as tk
from tkinter import messagebox

# 定义运算符
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def random_problem():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = round(operators.get(operation)(num_1, num_2), 2)  # 保留两位小数
    return num_1, operation, num_2, answer

class MathGame:
    def __init__(self, master):
        self.master = master
        self.master.title("数学游戏")
        self.score = 0

        self.question_label = tk.Label(master, text="")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="提交答案", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_question()

    def next_question(self):
        num_1, operation, num_2, self.correct_answer = random_problem()
        self.question_label.config(text=f'计算: {num_1} {operation} {num_2}')
        self.answer_entry.delete(0, tk.END)  # 清空输入框

    def check_answer(self):
        try:
            guess = float(self.answer_entry.get())
            if round(guess, 2) == self.correct_answer:
                self.score += 1
                messagebox.showinfo("正确", "回答正确！")
                self.next_question()
            else:
                messagebox.showinfo("错误", f"回答错误！正确答案是 {self.correct_answer}")
                messagebox.showinfo("游戏结束", f"你的得分是: {self.score}")
                self.master.quit()
        except ValueError:
            messagebox.showwarning("输入错误", "请输入一个有效的数字")

def start_game():
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()
   

if __name__ == "__main__":
    start_game()