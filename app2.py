import random
from flask import Flask, render_template, request

app2 = Flask(__name__)


def generate_fortune():
    fortunes = {
        "大吉": 5,
        "大吉2": 5,
        "吉": 15,
        "吉2": 15,
        "中吉": 15,
        "中吉2": 10,
        "小吉": 7,
        "小吉2": 8,
        "凶": 10,
        "凶2": 10,
    }

    outcomes = {
        "2項目": [
            "【恋愛】松尾芭蕉のように、感じたことを言葉で伝えましょう",  # 大吉
            "【学問】北と東の間がよいでしょう。旅の間に、地元の人と話してみるのも吉",  # 大吉2
            "【恋愛】新たな出会いや関係の発展が期待できるでしょう",  # 吉
            "【学問】予定が変わるかもしれません",  # 吉2
            "【恋愛】松尾芭蕉のように、感じたことを言葉で伝えましょう",  # 中吉
            "【学問】新たな発見や気づきがあなたを豊かにするでしょう",  # 中吉2
            "【恋愛】急速な変化はありません",  # 小吉
            "【学問】どこへ行っても良い気分転換になるでしょう",  # 小吉2
            "【恋愛】自己反省や改善点を見つけることで、関係を修復する道が開けるかもしれません",  # 凶
            "【学問】弁慶のような、旅のお供を探すと吉",  # 凶2
        ],
        "1項目": [
            "【願望】藤原秀衡の時代のごとく、大いに栄えるでしょう",
            "【商売】北と東の間がよいでしょう。旅の間に、地元の人と話してみるのも吉",
            "【願望】健康な体と心を大切にすれば大丈夫です",
            "【商売】予定が変わるかもしれません",
            "【願望】普段の生活での注意や予防策をしっかりと行いましょう",
            "【商売】新たな発見や気づきがあなたを豊かにするでしょう",
            "【願望】健康な体と心を大切にし、積極的に自己管理に努めましょう",
            "【商売】どこへ行っても良い気分転換になるでしょう",
            "【願望】ストレスや疲労に注意し、十分な睡眠をとることも重要です",
            "【商売】弁慶のような、旅のお供を探すと吉",
        ],
        # "【旅行】": [
        #     "北と東の間がよいでしょう。旅の間に、地元の人と話してみるのも吉",
        #     "予定が変わるかもしれません",
        #     "新たな発見や気づきがあなたを豊かにするでしょう",
        #     "どこへ行っても良い気分転換になるでしょう",
        #     "弁慶のような、旅のお供を探すと吉",
        # ],
        # "【商売】": [
        #     "あなたの才能と努力が開花し、大きな成功を収めることができるでしょう",
        #     "藤原秀衡の時代のごとく、大いに栄えるでしょう",
        #     "新しいプロジェクトやチャンスが舞い込むでしょう",
        #     "コツコツ取り組めば、成果を上げることができるでしょう",
        #     "成果や目標の達成には多くの努力が必要となるでしょう",
        # ],
        # "【学問】": [
        #     "自信を持って自分の能力を発揮できるでしょう",
        #     "あなたの努力や頑張りが実を結ぶでしょう",
        #     "努力や計画を続けることで、良い結果を得るでしょう",
        #     "大いに努力してください",
        #     "怠れば危ないです。諦めずに前向きな姿勢を持ち続けてください",
        # ],
        # "【争事】": [
        #     "チームワークや協力関係も円滑に進み、良い結果を生むでしょう",
        #     "柔軟性を持って対応しましょう",
        #     "波が立たずに収まるでしょう",
        #     "源義経と源頼朝のような関係にならないように気を付けましょう",
        #     "困難や障害が予想されます。相手を尊重する姿勢を持ちましょう",
        # ],
        # "【願望】": [
        #     "藤原清衡のごとく、理想の世界を築けるでしょう",
        #     "積極的に行動することで、成功への道を切り拓くことができるでしょう",
        #     "感謝の気持ちを怠らなければ喜び事が起きるでしょう",
        #     "努力や頑張りは必要ですが、焦る必要はありません",
        #     "困難を乗り越えるために、支えてくれる人々の力を借りて立ち向かいましょう",
        # ],
    }

    # Shuffle the list of fortunes
    shuffled_fortunes = list(fortunes.keys())
    random.shuffle(shuffled_fortunes)

    fortune = shuffled_fortunes.pop()

    if fortune == "大吉":
        key = 0

    elif fortune == "大吉2":
        key = 1

    elif fortune == "吉":
        key = 2

    elif fortune == "吉2":
        key = 3

    elif fortune == "中吉":
        key = 4

    elif fortune == "中吉2":
        key = 5

    elif fortune == "小吉":
        key = 6

    elif fortune == "小吉2":
        key = 7

    elif fortune == "凶":
        key = 8

    else:
        key = 9

    outcome_1 = outcomes["2項目"][key]
    outcome_2 = outcomes["1項目"][key]

    return (
        fortune,
        outcome_1,
        outcome_2,
    )


# Define the route for the index page
@app2.route("/top")
def show_top():
    return render_template("index.html")


@app2.route("/payment")
def show_payment():
    return render_template("payment")


@app2.route("/hiku")
def show_hiku():
    return render_template("hiku.html")


@app2.route("/result")
def show_omikuji():
    (
        fortune,
        outcome_1,
        outcome_2,
    ) = generate_fortune()
    return render_template(
        "result2.html",
        fortune=fortune,
        outcome_1=outcome_1,
        outcome_2=outcome_2,
    )


# プチ情報画面
@app2.route("/next", methods=["POST"])
def show_next():
    fortune = request.form["fortune"]

    if fortune == "大吉" or "大吉2":
        text = "晴れの日に食べるものと言えば、餅御膳！\n平泉では郷土料理としておもちが有名です。\n平泉でおもちを食べて、「大吉」のお祝いをしましょう！\nおめでどーごし!\n主なもち料理提供店一覧:"
        url = "https://hiraizu-meets.com/gourmet/"  # 実際のURLに置き換えてください
        # text = text.format(url)
        photo = "superbluck_petitinfo.jpg"

    elif fortune == "吉" or "吉2":
        text = "105年以上平泉で愛され続けてきた「弁慶力餅」を食べて､\n内なるエネルギーを蓄えましょう！\n※お土産屋さんや駅で見つけることができます｡\n本店は中尊寺通りへ｡"
        photo = "goodluck_petitinfo.jpg"
        url = ""

    elif fortune == "中吉" or "中吉2":
        text = "かつては京都についで2番目に栄えていたと言われる平泉｡\n心が平穏になれる静かな平泉を感じられるスポットで､\n平泉の空気を思いっきり吸ってみましょう｡\nおすすめスポット一覧 ***"
        photo = "fairygluck_petitinfo.jpg"
        url = ""

    elif fortune == "小吉" or "小吉2":
        text = "平泉で四季を感じるスポットへ行ってみましょう｡ \nきっと平泉の極楽浄土を感じられることでしょう｡ \nおすすめ平泉の四季\n 夏: 高舘から望む北上川と山\n秋: 毛越寺の紅葉"
        photo = "smallluck_petitinfo.jpg"
        url = ""

    else:
        text = "世界遺産の一つである無量光院から金鶏山に沈む夕日を眺めてみましょう｡\nきっと心が浄化されることでしょう｡\nけっぱれ~！"
        photo = "badluck_petitinfo.jpg"
        url = ""

    return render_template("petit_info.html", fortune=fortune, text=text, photo=photo, url=url)


if __name__ == "__main__":
    app2.run(debug=True, host="0.0.0.0", port=8000)
