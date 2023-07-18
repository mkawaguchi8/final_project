import random
from flask import Flask, render_template

app = Flask(__name__)


def generate_fortune():
    fortunes = {
        "大吉": 10,
        "吉": 30,
        "中吉": 25,
        "小吉": 15,
        "凶": 20
    }

    outcomes = {
        "願望": ["叶うでしょう", "なかなか叶わないかもしれません", "途中で諦めずに頑張りましょう"],
        "健康": ["元気に過ごせるでしょう", "ちょっと調子が崩れるかもしれません", "健康には気をつけましょう"],
        "失物": ["見つかるでしょう", "なかなか見つからないかもしれません", "探し続けてみましょう"],
        "旅行": ["楽しい旅行ができるでしょう", "予定が変わるかもしれません", "旅行の計画をしっかり立てましょう"],
        "商売": ["成功するでしょう", "売り上げが少し減るかもしれません", "努力を惜しまず頑張りましょう"],
        "学問": ["順調に進展するでしょう", "少し苦労するかもしれません", "諦めずに頑張りましょう"],
        "争事": ["円満に解決するでしょう", "少しトラブルが起きるかもしれません", "冷静な判断を心がけましょう"],
        "恋愛": ["素敵な出会いがあるでしょう", "恋の運気は少し低めかもしれません", "自分に自信を持ちましょう"],
        "平泉運": ["順調な運勢です", "ちょっと停滞気味かもしれません", "前向きな気持ちで過ごしましょう"]
    }

    # Shuffle the list of fortunes
    shuffled_fortunes = list(fortunes.keys())
    random.shuffle(shuffled_fortunes)

    fortune = shuffled_fortunes.pop()

    outcome = random.choice(list(outcomes.keys()))
    message = random.choice(outcomes[outcome])

    return fortune, outcome, message



@app.route("/")
def show_omikuji():
    fortune, outcome, message = generate_fortune()
    return render_template("result.html", fortune=fortune, outcome=outcome, message=message)


if __name__ == "__main__":
    app.run()
