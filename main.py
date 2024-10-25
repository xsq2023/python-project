import tkinter as tk
import subprocess
import webbrowser
import os
import Caterpillar
import color_game_main
import connect_four_main
# import dice_stimulator as dice_stimulator
import eggcatcher
import hangman
import letter_partner
import madlibs
import math_game
import sudoku
import tic_tac_toe_vs_computer
import p_2048
import snake
import train_snake
import train_2048

# 游戏文件夹路径
GAME_DIR = os.path.dirname(os.path.abspath(__file__))

def open_github():
    webbrowser.open("https://github.com")  # 替换为你的 GitHub 地址

# 启动游戏
def start_game(game_name):
    try:
        if game_name == "Caterpillar":
            Caterpillar.start()
        elif game_name == "color_game_main":
            color_game_main.start_game_window()
        elif game_name == "connect_four_main":
            connect_four_main.start_game_window()
        # elif game_name == "dice_stimulator":
        #     dice_stimulator.start_game()
        elif game_name == "eggcatcher":
            eggcatcher.start_egg_catcher_game()
        elif game_name == "hangman":
            hangman.start_game()
        elif game_name == "letter_partner":
            letter_partner.create_gui()
        elif game_name == "madlibs":
            madlibs.start_game()
        elif game_name == "math_game":
            math_game.start_game()
        elif game_name == "sudoku":
            sudoku.start_game()
        elif game_name == "tic_tac_toe_vs_computer":
            tic_tac_toe_vs_computer.start_game()
        elif game_name == "p_2048":
            p_2048.start_game()
        elif game_name == "snake":
            snake.start_game()
        elif game_name == "train_snake":
            train_snake.start_game_snake()  
        elif game_name == "train_2048":
            train_2048.start_game_2048()
        else:
            subprocess.Popen(['python', os.path.join(GAME_DIR, f"{game_name}.py")])
    except Exception as e:
        print(f"启动游戏 {game_name} 时出错: {e}")

# 启动训练模块
def start_training(module_name):
    try:
        if module_name == "train_2048":
            train_2048.start_training()
        elif module_name == "train_snake":
            train_snake.start_training()
    except Exception as e:
        print(f"启动训练模块 {module_name} 时出错: {e}")

# 创建游戏库界面
def create_game_library():
    library_window = tk.Toplevel()
    library_window.title("游戏库")
    library_window.geometry("500x500")

    game_list = [f[:-3] for f in os.listdir(GAME_DIR) if f.endswith('.py') and f not in ['main.py', 'train_2048.py', 'train_snake.py']]

    for game in game_list:
        button = tk.Button(library_window, text=game, command=lambda g=game: start_selected_game(g))
        button.pack(pady=5, fill=tk.X, expand=True)

    close_button = tk.Button(library_window, text="关闭", command=library_window.destroy)
    close_button.pack(pady=10)

def start_selected_game(game_name):
    start_game(game_name)

# 创建设置窗口
def create_settings_window(root):
    settings_window = tk.Toplevel()
    settings_window.title("设置")
    settings_window.geometry("300x200")

    def change_bg_color(color):
        root.configure(bg=color)

    # 颜色选择按钮
    tk.Button(settings_window, text="蓝色", command=lambda: change_bg_color("light blue")).pack(pady=5)
    tk.Button(settings_window, text="绿色", command=lambda: change_bg_color("light green")).pack(pady=5)
    tk.Button(settings_window, text="灰色", command=lambda: change_bg_color("light grey")).pack(pady=5)

    close_button = tk.Button(settings_window, text="关闭", command=settings_window.destroy)
    close_button.pack(pady=10)

# 创建主游戏窗口
def create_main_window():
    root = tk.Tk()
    root.title("主游戏窗口")
    root.geometry("400x400")

    # GitHub按钮
    github_button = tk.Button(root, text="点击进入GitHub项目界面", command=open_github)
    github_button.pack(side="left", padx=20, pady=10, anchor="sw")  # 将按钮放在左下角

    # 作者标签
    author_label = tk.Label(root, text="作者: 信息安全-xsq", anchor="se")
    author_label.pack(side="bottom", padx=10, pady=5, anchor="se")

    # 提示信息标签
    instructions_label = tk.Label(root, text="请先看readme.md文件再进行使用", fg="red", anchor="se")
    instructions_label.pack(side="bottom", padx=10, pady=0, anchor="se")

    start_button = tk.Button(root, text="进入游戏库", command=create_game_library)
    start_button.pack(pady=20)

    show_games_button = tk.Button(root, text="显示游戏列表", command=lambda: show_game_list(root))
    show_games_button.pack(pady=10)

    training_button = tk.Button(root, text="自动模块", command=create_training_window)
    training_button.pack(pady=10)

    # 设置按钮
    settings_button = tk.Button(root, text="设置", command=lambda: create_settings_window(root))
    settings_button.pack(pady=10)

    # 退出按钮
    exit_button = tk.Button(root, text="退出", command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()


# 显示游戏列表
def show_game_list(root):
    game_list_window = tk.Toplevel(root)
    game_list_window.title("游戏列表")
    game_list_window.geometry("500x500")

    game_list = [f[:-3] for f in os.listdir(GAME_DIR) if f.endswith('.py') and f not in ['main.py', 'train_2048', 'train_snake']]

    for game in game_list:
        label = tk.Label(game_list_window, text=game)
        label.pack(pady=5)

    close_button = tk.Button(game_list_window, text="关闭", command=game_list_window.destroy)
    close_button.pack(pady=10)

# 创建训练模块窗口
def create_training_window():
    training_window = tk.Toplevel()
    training_window.title("训练模块")
    training_window.geometry("300x200")

    train_2048_button = tk.Button(training_window, text="自动-2048", command=train_2048.start_game_2048)
    train_2048_button.pack(pady=10)

    train_snake_button = tk.Button(training_window, text="自动-Snake", command=train_snake.start_game_snake)
    train_snake_button.pack(pady=10)

    close_button = tk.Button(training_window, text="关闭", command=training_window.destroy)
    close_button.pack(pady=10)


if __name__ == "__main__":
    print("请先看readme.md文件再进行使用")
    

# 直接调用创建主游戏窗口
    create_main_window()
