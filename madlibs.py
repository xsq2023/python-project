import random
import tkinter as tk

# 随机词汇库
nouns = ["猫", "狗", "汽车", "房子", "书", "电脑", "比萨", "球", "花", "朋友", "星星", "音乐"]
plural_nouns = ["猫咪", "狗狗", "汽车", "房屋", "书籍", "电脑", "比萨", "球", "花朵", "朋友们", "星星们"]
adjectives = ["美丽的", "丑陋的", "快乐的", "伤心的", "大的", "小的", "快的", "慢的", "神奇的", "古怪的"]
adverbs = ["快速地", "安静地", "快乐地", "伤心地", "大声地", "轻轻地", "神秘地", "突然地"]

scenes = [
    "学校聚会的趣事",
    "露营惊险夜",
    "生日派对的意外",
    "太空探险",
    "魔法城堡的奇遇"
]

class MadLibsGame:
    def __init__(self, master):
        self.master = master
        master.title("随机场景填词游戏")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="输入名词1:").pack()
        self.entry_noun1 = tk.Entry(self.master)
        self.entry_noun1.pack()

        tk.Label(self.master, text="输入名词2:").pack()
        self.entry_noun2 = tk.Entry(self.master)
        self.entry_noun2.pack()

        tk.Label(self.master, text="输入名词3:").pack()
        self.entry_noun3 = tk.Entry(self.master)
        self.entry_noun3.pack()

        tk.Label(self.master, text="输入复数名词1:").pack()
        self.entry_plural1 = tk.Entry(self.master)
        self.entry_plural1.pack()

        tk.Label(self.master, text="输入复数名词2:").pack()
        self.entry_plural2 = tk.Entry(self.master)
        self.entry_plural2.pack()

        tk.Label(self.master, text="输入形容词1:").pack()
        self.entry_adj1 = tk.Entry(self.master)
        self.entry_adj1.pack()

        tk.Label(self.master, text="输入形容词2:").pack()
        self.entry_adj2 = tk.Entry(self.master)
        self.entry_adj2.pack()

        tk.Label(self.master, text="输入副词1:").pack()
        self.entry_adv1 = tk.Entry(self.master)
        self.entry_adv1.pack()

        tk.Label(self.master, text="输入副词2:").pack()
        self.entry_adv2 = tk.Entry(self.master)
        self.entry_adv2.pack()

        tk.Button(self.master, text="生成故事", command=self.mad_libs).pack()

        self.text_output = tk.Text(self.master, height=15, width=60)
        self.text_output.pack()

    def mad_libs(self):
        scene = random.choice(scenes)

        # 收集用户输入
        noun1 = self.entry_noun1.get() or random.choice(nouns)
        noun2 = self.entry_noun2.get() or random.choice(nouns)
        noun3 = self.entry_noun3.get() or random.choice(nouns)
        plural1 = self.entry_plural1.get() or random.choice(plural_nouns)
        plural2 = self.entry_plural2.get() or random.choice(plural_nouns)
        adjective1 = self.entry_adj1.get() or random.choice(adjectives)
        adjective2 = self.entry_adj2.get() or random.choice(adjectives)
        adverb1 = self.entry_adv1.get() or random.choice(adverbs)
        adverb2 = self.entry_adv2.get() or random.choice(adverbs)

        # 根据场景输出生成的故事
        story = self.generate_story(scene, noun1, noun2, noun3, plural1, plural2, adjective1, adjective2, adverb1, adverb2)

        # 显示生成的故事
        self.text_output.delete(1.0, tk.END)  # 清空之前的内容
        self.text_output.insert(tk.END, story)  # 插入新的故事

    def generate_story(self, scene, noun1, noun2, noun3, plural1, plural2, adjective1, adjective2, adverb1, adverb2):
        if scene == "学校聚会的趣事":
            return f"""在学校的聚会上，学生们准备了一些 {noun1} 和 {noun2} 来庆祝。{adjective1} 的音乐响起，大家开始 {adverb1} 跳舞，气氛十分热烈。
            突然，一位老师发现了不合适的 {plural1}，于是大喊：“这里不能吃 {plural2}！”大家都 {adverb2} 地笑了。
            在这个欢乐的时刻，许多同学开始分享他们的趣事，甚至还有人带来了搞笑的表演，整场聚会充满了欢声笑语。"""

        elif scene == "露营惊险夜":
            return f"""一群朋友在森林里露营，他们准备了 {noun1} 和 {noun2}，但晚上突然下起了 {plural1}。在篝火旁，大家讲起了 {adjective1} 的鬼故事。
            随着故事的深入，气氛越来越紧张。结果一只 {noun3} 突然出现，吓得他们 {adverb1} 逃跑。
            他们跑到一棵大树下，发现那只 {noun3} 原来是迷路的，眼中流露出好奇的神情。于是，他们决定一起 {adverb2} 地帮助它，最终在星空下建立了深厚的友谊。"""

        elif scene == "生日派对的意外":
            return f"""在朋友的生日派对上，准备了许多美味的 {noun1} 和 {noun2}。聚会上，大家一起 {adverb1} 唱歌，祝他生日快乐。
            忽然，一个 {noun3} 从蛋糕里跳出来，大家都惊讶地 {adverb2} 大叫。为了庆祝，他们决定围成一圈，共同分享这个惊喜。
            接着，朋友们开始互相交换礼物，每个人的笑声和祝福交织在一起，直到最后，他们围坐在一起，分享着各自的故事和梦想，整个派对充满了温馨与欢乐。"""

        elif scene == "太空探险":
            return f"""宇航员们在太空站上准备了一些 {noun1} 和 {noun2} 来庆祝他们的成功任务。为了庆祝这次的成就，他们计划了一场盛大的聚会。
            突然，他们发现了一个 {noun3} 在太空漂浮，大家都 {adverb1} 地想抓住它。经过一番努力，他们终于成功将其抓住并带回飞船。
            在飞船上，他们兴奋地讨论这次探险的意义，甚至开始计划下一次的任务，梦想着更远的星际旅行与未知的冒险，这让他们充满了期待和激情。"""

        elif scene == "魔法城堡的奇遇":
            return f"""在一个魔法城堡里，巫师们正在准备神奇的 {noun1} 和 {noun2}。他们的目标是变出一个 {noun3}，但由于 {adjective1} 的咒语，意外地召唤出了一个 {plural1}。
            整个城堡瞬间变得一团糟，巫师们齐心协力 {adverb1} 地解决问题，然而不久后又出现了新的麻烦，他们发现原本的咒语似乎还有未完成的部分。
            于是，巫师们开始寻找新的方法，经过一番波折，他们最终通过团队合作，成功地恢复了城堡的和平与秩序，成为了令人称赞的英雄。"""

def start_game():
    root = tk.Tk()
    game = MadLibsGame(root)
    root.mainloop()
    

if __name__ == "__main__":
    start_game()