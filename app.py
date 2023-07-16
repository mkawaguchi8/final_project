import tkinter as tk
import random


def omikuji():
    fortunes = [
        "Great fortune awaits you!",
        "Good luck is coming your way!",
        "Be cautious, bad luck is near.",
        "A surprise is waiting for you!",
        "Your hard work will pay off soon.",
        "Take care of your health.",
        "Unexpected visitors will bring you joy.",
        "Today is your lucky day!",
        "Stay positive and good things will happen.",
        "Be patient, good things take time.",
    ]

    return random.choice(fortunes)


def shake_omikuji():
    fortune_text.set(omikuji())


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Omikuji App")

fortune_text = tk.StringVar()

welcome_label = tk.Label(root, text="Welcome to the Omikuji app!", font=("Arial", 16))
welcome_label.pack(pady=10)

omikuji_button = tk.Button(
    root, text="Shake the Omikuji", command=shake_omikuji, font=("Arial", 14), padx=20, pady=10
)
omikuji_button.pack(pady=10)

fortune_label = tk.Label(root, textvariable=fortune_text, font=("Arial", 14), wraplength=300)
fortune_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app, font=("Arial", 12), padx=10, pady=5)
exit_button.pack(pady=10)

root.mainloop()

# Minori おなかすいた~~~
