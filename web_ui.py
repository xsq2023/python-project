from flask import Flask, render_template, redirect, url_for
import subprocess
import os

app = Flask(__name__)

# 修改为当前目录
GAME_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    # 获取当前目录下的所有 Python 文件（游戏模块）
    games = [f[:-3] for f in os.listdir(GAME_DIR) if f.endswith('.py') and f != 'app.py']
    return render_template('index.html', games=games)

@app.route('/start_game/<game_name>')
def start_game(game_name):
    try:
        subprocess.Popen(['python', os.path.join(GAME_DIR, f"{game_name}.py")])
    except Exception as e:
        print(f"启动游戏 {game_name} 时出错: {e}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
