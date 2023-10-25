import random
import webbrowser
import paypayopa
import time
from flask import Flask, render_template, request, url_for, make_response, redirect

app = Flask(__name__)

# QR決済画面


@app.route("/payment")
def payment():
    API_KEY = "a_VO0IMBderf_sfC9"
    API_SECRET = "+tSBbY27/UXSTTqyPYQWZHvkj+5Bm3b+vK0hIaxpTqI="
    client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
    client.set_assume_merchant("683243483900723200")

    redirect_url = url_for("show_hiku", _external=True)

    request = {
        "merchantPaymentId": round(time.time()),  # => 加盟店発番のユニークな決済取引ID
        "codeType": "ORDER_QR",
        "redirectUrl": redirect_url,
        "redirectType": "WEB_LINK",
        "orderDescription": "Example - test",
        "orderItems": [
            {
                "name": "test",
                "category": "omikuji",
                "quantity": 1,
                "productId": "0001",
                "unitPrice": {"amount": 100, "currency": "JPY"},
            }
        ],
        "amount": {"amount": 100, "currency": "JPY"},
    }

    response = client.Code.create_qr_code(request)
    qr_code_url = response["data"]["deeplink"]

    return redirect(qr_code_url)


# おみくじ画面
def generate_fortune():
    fortunes = {"大吉": 10, "吉": 30, "中吉": 25, "小吉": 15, "凶": 20}

    outcomes = {
        "【恋愛】": [
            "素晴らしい出会いや深い絆を築けるでしょう",
            "新たな出会いや関係の発展が期待できるでしょう",
            "松尾芭蕉のように、感じたことを言葉で伝えましょう",
            "急速な変化はありません",
            "自己反省や改善点を見つけることで、関係を修復する道が開けるかもしれません",
        ],
        "【健康】": [
            "エネルギーや活力に満ち溢れています",
            "健康な体と心を大切にすれば大丈夫です",
            "普段の生活での注意や予防策をしっかりと行いましょう",
            "健康な体と心を大切にし、積極的に自己管理に努めましょう",
            "ストレスや疲労に注意し、十分な睡眠をとることも重要です",
        ],
        "【失物】": [
            "すぐに出てくるでしょう",
            "必ず出ます",
            "早く探しましょう",
            "遅れますが必ず出るでしょう",
            "あきらめずに待ち続けましょう",
        ],
        "【旅行】": [
            "北と東の間がよいでしょう。旅の間に、地元の人と話してみるのも吉",
            "予定が変わるかもしれません",
            "新たな発見や気づきがあなたを豊かにするでしょう",
            "どこへ行っても良い気分転換になるでしょう",
            "弁慶のような、旅のお供を探すと吉",
        ],
        "【商売】": [
            "あなたの才能と努力が開花し、大きな成功を収めることができるでしょう",
            "藤原秀衡の時代のごとく、大いに栄えるでしょう",
            "新しいプロジェクトやチャンスが舞い込むでしょう",
            "コツコツ取り組めば、成果を上げることができるでしょう",
            "成果や目標の達成には多くの努力が必要となるでしょう",
        ],
        "【学問】": [
            "自信を持って自分の能力を発揮できるでしょう",
            "あなたの努力や頑張りが実を結ぶでしょう",
            "努力や計画を続けることで、良い結果を得るでしょう",
            "大いに努力してください",
            "怠れば危ないです。諦めずに前向きな姿勢を持ち続けてください",
        ],
        "【争事】": [
            "チームワークや協力関係も円滑に進み、良い結果を生むでしょう",
            "柔軟性を持って対応しましょう",
            "波が立たずに収まるでしょう",
            "源義経と源頼朝のような関係にならないように気を付けましょう",
            "困難や障害が予想されます。相手を尊重する姿勢を持ちましょう",
        ],
        "【願望】": [
            "藤原清衡のごとく、理想の世界を築けるでしょう",
            "積極的に行動することで、成功への道を切り拓くことができるでしょう",
            "感謝の気持ちを怠らなければ喜び事が起きるでしょう",
            "努力や頑張りは必要ですが、焦る必要はありません",
            "困難を乗り越えるために、支えてくれる人々の力を借りて立ち向かいましょう",
        ],
        # "【スパルタキャンプ運】": [
        # "素晴らしい結果を残しました！",
        # "三浦さんも喜んでます！",
        # "プログラマーへの第一歩です！",
        # "キャンプが終わっても勉強を続けましょう！",
        # "もう少し頑張れたんじゃない？",
        # ],
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

    outcome_1 = outcomes["【恋愛】"][key]
    outcome_2 = outcomes["【健康】"][key]
    outcome_3 = outcomes["【失物】"][key]
    outcome_4 = outcomes["【旅行】"][key]
    outcome_5 = outcomes["【商売】"][key]
    outcome_6 = outcomes["【学問】"][key]
    outcome_7 = outcomes["【争事】"][key]
    outcome_8 = outcomes["【願望】"][key]
    # outcome_9 = outcomes["【スパルタキャンプ運】"][key]

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
        # outcome_9,
    )


# Define the route for the index page
@app.route("/top")
def show_top():
    return render_template("index.html")


@app.route("/payment")
def show_payment():
    return render_template("payment")


@app.route("/hiku")
def show_hiku():
    return render_template("hiku.html")


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
        # outcome_9,
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
        # outcome_9=outcome_9,
    )


# プチ情報画面
@app.route("/next", methods=["POST"])
def show_next():
    fortune = request.form["fortune"]

    if fortune == "大吉":
        text = "晴れの日に食べるものと言えば、餅御膳！\n平泉では郷土料理としておもちが有名です。\n平泉でおもちを食べて、「大吉」のお祝いをしましょう！\nおめでどーごし!\n主なもち料理提供店一覧:"
        url = "https://hiraizu-meets.com/gourmet/"  # 実際のURLに置き換えてください
        # text = text.format(url)
        photo = "superbluck_petitinfo.jpg"

    elif fortune == "吉":
        text = "105年以上平泉で愛され続けてきた「弁慶力餅」を食べて､\n内なるエネルギーを蓄えましょう！\n※お土産屋さんや駅で見つけることができます｡\n本店は中尊寺通りへ｡"
        photo = "goodluck_petitinfo.jpg"
        url = ""

    elif fortune == "中吉":
        text = "かつては京都についで2番目に栄えていたと言われる平泉｡\n心が平穏になれる静かな平泉を感じられるスポットで､\n平泉の空気を思いっきり吸ってみましょう｡\nおすすめスポット一覧 ***"
        photo = "fairygluck_petitinfo.jpg"
        url = ""

    elif fortune == "小吉":
        text = "平泉で四季を感じるスポットへ行ってみましょう｡ \nきっと平泉の極楽浄土を感じられることでしょう｡ \nおすすめ平泉の四季\n 夏: 高舘から望む北上川と山\n秋: 毛越寺の紅葉"
        photo = "smallluck_petitinfo.jpg"
        url = ""

    else:
        text = "世界遺産の一つである無量光院から金鶏山に沈む夕日を眺めてみましょう｡\nきっと心が浄化されることでしょう｡\nけっぱれ~！"
        photo = "badluck_petitinfo.jpg"
        url = ""

    return render_template("petit_info.html", fortune=fortune, text=text, photo=photo, url=url)


def generate_fortune_eng():
    fortunes = {
        "Superb Luck": 10,
        "Good Luck": 30,
        "Fairly Good Luck": 25,
        "Small Luck": 15,
        "Bad Luck": 20,
    }

    outcomes = {
        "【DESIRE】": [
            "You will be able to build an ideal world like Fujiwara-no-Kiyohira.",
            "By taking proactive actions, you will be able to pave the way to success.",
            "If you accept the feelings of gratitude, joy will occur.",
            "Effort and hard work are necessary, but no rushing.",
            "To overcome difficulties, face them with support from others.",
        ],
        "【HEALTH】": [
            "You are filled with energy and vitality.",
            "You will be fine if you take care of your body and mind.",
            "Let's pay attention to our daily lives and take preventive measures seriously.",
            "Take good care of your body and mind, and actively work on self-management.",
            "Be mindful of stress and fatigue. Getting a quality sleep is very important.",
        ],
        "【LOST PROPERTY】": [
            "It will come out soon.",
            "It will definitely be found.",
            "Let's search for it quickly.",
            "May be delayed, but will definitely be found.",
            "Keep waiting, and don't give up.",
        ],
        "【TRAVEL】": [
            "Northeast areas would be favorable. During your journey, it is encouraged to talk to the locals.",
            "Your plans may change.",
            "New discoveries and realizations will enrich you.",
            "No matter where you go, it will be a good change of pace.",
            "Let's immerse ourselves more in the local food, culture, and history.",
            "It's fortunate to seek travel companions like Benkei.",
        ],
        "【BUSINESS】": [
            "Your talent and efforts will blossom, and you will achieve great success.",
            "Just like during the time of Fujiwara no Hidehira, you will prosper greatly.",
            "New projects and opportunities will come your way.",
            "If you work diligently and steadily, you will achieve great results.",
            "Achieving results and goals will require a lot of effort.",
        ],
        "【ACADEMICS】": [
            "You will be able to confidently demonstrate your abilities.",
            "Your efforts and hard work will pay off.",
            "By continuing your efforts and planning, you will achieve good results.",
            "Work hard.",
            "It's risky to neglect. Continue with a positive attitude without giving up.",
        ],
        "【CONFLICT】": [
            "Teamwork and cooperation will progress smoothly, leading to positive outcomes.",
            "Handle it with flexibility and adaptability",
            "The situation will settle without causing major disturbances.",
            "Be careful not to develop a relationship like that of Minamoto-no-Yoshitsune and Minamoto-no-Yoritomo.",
            "Difficulties and obstacles are expected. Maintain a respectful attitude towards others.",
        ],
        "【ROMANCE】": [
            "You will be able to encounter wonderful and deep connections.",
            "Expect new encounters and the development of relationships.",
            "Like Matsuo Basho, express your feelings through words.",
            "There won't be any sudden changes.",
            "By self-reflection, you may be able to repair the relationship soon.",
        ],
        # "【平泉運】": ["考え中", "考え中", "考え中", "考え中", "考え中"],
    }

    # Shuffle the list of fortunes
    shuffled_fortunes = list(fortunes.keys())
    random.shuffle(shuffled_fortunes)

    fortune = shuffled_fortunes.pop()

    if fortune == "Superb Luck":
        key = 0

    elif fortune == "Good Luck":
        key = 1

    elif fortune == "Fairly Good Luck":
        key = 2

    elif fortune == "Small Luck":
        key = 3

    else:
        key = 4

    outcome_1 = outcomes["【DESIRE】"][key]
    outcome_2 = outcomes["【HEALTH】"][key]
    outcome_3 = outcomes["【LOST PROPERTY】"][key]
    outcome_4 = outcomes["【TRAVEL】"][key]
    outcome_5 = outcomes["【BUSINESS】"][key]
    outcome_6 = outcomes["【ACADEMICS】"][key]
    outcome_7 = outcomes["【CONFLICT】"][key]
    outcome_8 = outcomes["【ROMANCE】"][key]
    # outcome_9 = outcomes["【平泉運】"][key]

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
        # outcome_9,
    )


@app.route("/top_eng")
def show_top_eng():
    return render_template("indexeng.html")


@app.route("/hiku_eng")
def show_hiku_eng():
    return render_template("hikueng.html")


@app.route("/result_eng")
def show_omikuji_eng():
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
        # outcome_9,
    ) = generate_fortune_eng()
    return render_template(
        "resulteng.html",
        fortune=fortune,
        outcome_1=outcome_1,
        outcome_2=outcome_2,
        outcome_3=outcome_3,
        outcome_4=outcome_4,
        outcome_5=outcome_5,
        outcome_6=outcome_6,
        outcome_7=outcome_7,
        outcome_8=outcome_8,
        # outcome_9=outcome_9,
    )


@app.route("/next_eng", methods=["POST"])
def show_next_eng():
    fortune = request.form["fortune"]

    if fortune == "Superb Luck":
        text = "Speaking of what to eat on a sunny day, it's mochi gozen! In Hiraizumi, mochi (rice cakes) is famous as a local dish. Let's have mochi in Hiraizumi and celebrate with Great Fortune! Congratulations!"
        photo = "superbluck_petitinfo.jpg"

    elif fortune == "Good Luck":
        text = "Let's eat Benkei-no-Chikara-Mochi, which has been loved in Hiraizumi for over 105 years, and store your inner energy! You can find it at souvenir shops or the station. The main store is located on Chusonji Street."
        photo = "goodluck_petitinfo.jpg"

    elif fortune == "Fairly Good Luck":
        text = "Hiraizumi, once said to be the second most prosperous city after Kyoto. Let's feel the serene and quiet atmosphere of Hiraizumi, where our hearts can find tranquility. Take a deep breath of Hiraizumi's air and immerse yourself in its essence. Recommended to visit Genbikei Gorge and Mount Kinkeisan."
        photo = "fairygluck_petitinfo.jpg"

    elif fortune == "Small Luck":
        text = "Let's visit the spots in Hiraizumi to experience the four seasons. You will surely feel the blissful paradise of Hiraizumi. Recommended to see the view of the Kitakami River and the mountains from Takadate in the summer, as well as the leaf foliage at Motsuji Temple in the fall."
        photo = "smallluck_petitinfo.jpg"

    else:
        text = "Let's gaze at the sunset sinking behind Mount Kinkazan from Muryokoin, one of the World Heritage sites. It will surely purify our hearts. Enjoy the moment!"
        photo = "badluck_petitinfo.jpg"

    return render_template("petit_infoeng.html", fortune=fortune, text=text, photo=photo)


if __name__ == "__main__":
    app.run()
