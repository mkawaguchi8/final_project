import tkinter as tk
import random

def shake_fortune_stick():
    fortunes = [
        "大吉 - すべてのことが順調に運びます。",
        "中吉 - ほぼすべてのことが順調に運びます。",
        "小吉 - いくつかのことが順調に運びます。",
        "末吉 - わずかな幸運があります。",
        "凶 - 幸運と不運が半々です。",
        "大凶 - すべてのことがうまくいきません。"
    ]

    selected_fortune = random.choice(fortunes)
    result_label.config(text=selected_fortune)

# Tkinterウィンドウの作成
window = tk.Tk()
window.title("おみくじ")
window.geometry("300x200")

# 画像表示用のCanvas
canvas = tk.Canvas(window, width=150, height=150)
canvas.pack(pady=20)

# 筒の画像を表示
tube_img = tk.PhotoImage(file="path/to/tube_image.png")  # 画像ファイルのパスを指定
canvas.create_image(75, 75, image=tube_img)

# おみくじを引くボタン
shake_button = tk.Button(window, text="おみくじを引く", command=shake_fortune_stick)
shake_button.pack()

# 運勢結果を表示するラベル
result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# ウィンドウを開始
window.mainloop()
