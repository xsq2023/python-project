import tkinter as tk
from tkinter import messagebox

def play_game(word):
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    list2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    prepartner = []
    postpartner = []
    
    for i in word:
        if i in list1:
            prepartner.append(i)
        elif i in list2:
            postpartner.append(i)

    if not all(list2[list1.index(p)] in postpartner for p in prepartner):
        return "YOU LOST"
    
    prepartner1 = prepartner.copy()
    postpartner1 = postpartner.copy()
    
    to_remove = []

    for k in prepartner:
        try:
            x = prepartner.index(k)
            y = postpartner.index(list2[list1.index(k)])
            
            if word.index(prepartner[x]) < word.index(postpartner[y]):
                if word.index(postpartner[y]) - word.index(prepartner[x]) == 1:
                    to_remove.append((x, y))
            else:
                return "YOU LOST"
        except ValueError:
            return "Invalid character in input."

    for x, y in reversed(to_remove):
        if x < len(prepartner1) and y < len(postpartner1):
            prepartner1.pop(x)
            postpartner1.pop(y)

    count = 0
    for l in prepartner1:
        if prepartner1.index(l) == postpartner1.index(list2[list1.index(l)]):
            count += 1
    
    if count == len(prepartner1):
        return "GAME WON"
    else:
        return "GAME LOST"

def submit_word():
    word = entry.get()
    result = play_game(word)
    messagebox.showinfo("Result", result)

def create_gui():
    root = tk.Tk()
    root.title("字母配对游戏")

    instruction = """游戏规则：
输入单词: 玩家输入一个字母组成的单词，该单词可以包含来自两个字母列表的字母。
前伴随字母（prepartners）: 属于字母列表 list1 的字母（a 到 m）。
后伴随字母（postpartners）: 属于字母列表 list2 的字母（n 到 z）。

字母配对: 每个前伴随字母都有一个对应的后伴随字母，具体是通过它们在 list1 和 list2 中的位置确定的。例如，a 对应 n，b 对应 o，依此类推。

必须存在配对: 每个前伴随字母必须有对应的后伴随字母。如果缺少某个后伴随字母，游戏结束，输出“YOU LOST”。
顺序检查: 前伴随字母在单词中的位置必须在其对应后伴随字母的前面，并且两者之间的距离必须为 1。如果不满足这一条件，游戏结束，输出“YOU LOST”。
胜利条件: 如果所有前伴随字母都有有效的配对且满足顺序条件，玩家获胜，输出“GAME WON”。"""
    
    label = tk.Label(root, text=instruction, justify=tk.LEFT, padx=10, pady=10)
    label.pack()

    entry_label = tk.Label(root, text="请输入一个单词:")
    entry_label.pack(pady=5)

    global entry
    entry = tk.Entry(root)
    entry.pack(pady=5)

    submit_button = tk.Button(root, text="提交", command=submit_word)
    submit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
