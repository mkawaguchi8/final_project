import random
from flask import Flask, render_template, request

app = Flask(__name__)


def generate_fortune():
    fortunes = {"大吉": 10, "吉": 30, "中吉": 25, "小吉": 15, "凶": 20}

    outcomes = {
        "願望": [
            "藤原清衡のごとく、理想の世界を築けるでしょう",
            "積極的に行動することで、成功への道を切り拓くことができるでしょう",
            "感謝の気持ちを怠らなければ喜び事が起きるでしょう",
            "努力や頑張りは必要ですが、焦る必要はありません",
            "困難を乗り越えるために、支えてくれる人々の力を借りて立ち向かいましょう",
        ],
        "健康": [
            "エネルギーや活力に満ち溢れています",
            "健康な体と心を大切にすれば大丈夫です",
            "普段の生活での注意や予防策をしっかりと行いましょう",
            "健康な体と心を大切にし、積極的に自己管理に努めましょう",
            "ストレスや疲労に注意し、十分な睡眠をとることも重要です",
        ],
        "失物": [
            "すぐに出てくるでしょう",
            "必ず出ます",
            "早く探しましょう",
            "遅れますが必ず出るでしょう",
            "あきらめずに待ち続けましょう",
        ],
        "旅行": [
            "北と東の間がよいでしょう。旅の間に、地元の人と話してみるのも吉",
            "予定が変わるかもしれません",
            "新たな発見や気づきがあなたを豊かにするでしょう",
            "どこへ行っても良い気分転換になるでしょう",
            "現地の食、文化、歴史にもっと触れましょう",
            "弁慶のような、旅のお供を探すと吉",
        ],
        "商売": [
            "あなたの才能と努力が開花し、大きな成功を収めることができるでしょう",
            "藤原秀衡の時代のごとく、大いに栄えるでしょう",
            "新しいプロジェクトやチャンスが舞い込むでしょう",
            "コツコツ取り組めば、成果を上げることができるでしょう",
            "成果や目標の達成には多くの努力が必要となるでしょう",
        ],
        "学問": [
            "自信を持って自分の能力を発揮できるでしょう",
            "あなたの努力や頑張りが実を結ぶでしょう",
            "努力や計画を続けることで、良い結果を得るでしょう",
            "大いに努力してください",
            "怠れば危ないです。諦めずに前向きな姿勢を持ち続けてください",
        ],
        "争事": [
            "チームワークや協力関係も円滑に進み、良い結果を生むでしょう",
            "柔軟性を持って対応しましょう",
            "波が立たずに収まるでしょう",
            "源義経と源頼朝のような関係にならないように気を付けましょう",
            "困難や障害が予想されます。相手を尊重する姿勢を持ちましょう",
        ],
        "恋愛": [
            "素晴らしい出会いや深い絆を築けるでしょう",
            "新たな出会いや関係の発展が期待できるでしょう",
            "松尾芭蕉のように、感じたことを言葉で伝えましょう",
            "急速な変化はありません",
            "自己反省や改善点を見つけることで、関係を修復する道が開けるかもしれません",
        ],
        "平泉運": ["考え中", "考え中", "考え中", "考え中", "考え中"],
    }

    # Shuffle the list of fortunes
    shuffled_fortunes = list(fortunes.keys())
    random.shuffle(shuffled_fortunes)

    fortune = shuffled_fortunes.pop()

    if fortune == "大吉":
        key = 0

    elif fortune == "吉":
        key = 1

    elif fortune == "中吉":
        key = 2

    elif fortune == "小吉":
        key = 3

    else:
        key = 4

    outcome_1 = outcomes["願望"][key]
    outcome_2 = outcomes["健康"][key]
    outcome_3 = outcomes["失物"][key]
    outcome_4 = outcomes["旅行"][key]
    outcome_5 = outcomes["商売"][key]
    outcome_6 = outcomes["学問"][key]
    outcome_7 = outcomes["争事"][key]
    outcome_8 = outcomes["恋愛"][key]
    outcome_9 = outcomes["平泉運"][key]

    return (
        fortune,
        outcome_1,
        outcome_2,
        outcome_3,
        outcome_4,
        outcome_5,
        outcome_6,
        outcome_7,
        outcome_8,
        outcome_9,
    )


@app.route("/result")
def show_omikuji():
    (
        fortune,
        outcome_1,
        outcome_2,
        outcome_3,
        outcome_4,
        outcome_5,
        outcome_6,
        outcome_7,
        outcome_8,
        outcome_9,
    ) = generate_fortune()
    return render_template(
        "result.html",
        fortune=fortune,
        outcome_1=outcome_1,
        outcome_2=outcome_2,
        outcome_3=outcome_3,
        outcome_4=outcome_4,
        outcome_5=outcome_5,
        outcome_6=outcome_6,
        outcome_7=outcome_7,
        outcome_8=outcome_8,
        outcome_9=outcome_9,
    )


@app.route("/next", methods=["POST"])
def show_next():
    fortune = request.form["fortune"]

    if fortune == "大吉":
        text = "晴れの日に食べるものと言えば、餅御膳！平泉では郷土料理としておもちが有名です。平泉でおもちを食べて、「大吉」のお祝いをしましょう！おめでどーごし※主なもち食提供店一覧 URL"

    elif fortune == "吉":
        text = "105年以上平泉で愛され続けてきた「弁慶の力餅」を食べて､内なるエネルギーを蓄えましょう！※お土産屋さんや駅で見つけることができます｡本店は中尊寺通りへ｡"
    
    elif fortune == "中吉":
        text = "かつては京都についで2番目に栄えていたと言われる平泉｡心が平穏になれる静かな平泉を感じられるスポットで､平泉の空気を思いっきり吸ってみましょう｡おすすめスポット"

    elif fortune == "小吉":
        text = "平泉で四季を感じるスポットへ行ってみましょう｡ きっと平泉の極楽浄土を感じられることでしょう｡ おすすめ平泉の四季 夏: 高舘から望む北上川と山 秋: 毛越寺の紅葉"

    else:
        text = "世界遺産の一つである無量光院から金鶏山に沈む夕日を眺めてみましょう｡きっと心が浄化されることでしょう｡けっぱれ~！"

    return render_template("petit_info.html", fortune=fortune, text=text)




if __name__ == "__main__":
    app.run(port=8002, debug=True)
