import tkinter as tk
from tkinter import messagebox
import random

def show_random_result():
    results = [
        "大吉：すべての願いが叶います。",
        "中吉：多くの願いが叶います。",
        "小吉：いくつかの願いが叶います。",
        "吉：願いが一部叶います。",
        "末吉：願いの達成には努力が必要です。",
        "凶：願いが叶わないこともあります。",
        "大凶：避けた方が良い行動を示しています。"
    ]

    result = random.choice(results)
    messagebox.showinfo("おみくじの結果", result)

# GUIアプリケーションの作成
app = tk.Tk()
app.title("おみくじ")

# おみくじの筒の画像を表示するためのラベル
omikuji_img = tk.PhotoImage(file="omikuji_tube.png")
omikuji_label = tk.Label(app, image=omikuji_img)
omikuji_label.pack()

# おみくじの筒の画像をクリックしたときにランダムな結果を表示するボタン
omikuji_button = tk.Button(app, text="おみくじを引く", command=show_random_result)
omikuji_button.pack()

app.mainloop()
