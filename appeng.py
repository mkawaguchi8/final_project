import random
from flask import Flask, render_template, request

app = Flask(__name__)


def generate_fortune():
    fortunes = {"Superb Luck": 10, "Good Luck": 30, "Fairly Good Luck": 25, "Small Luck": 15, "Bad Luck": 20}

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


@app.route("/next", methods=["POST"])
def show_next():
    fortune = request.form["fortune"]

    if fortune == "Superb Luck":
        text = "Speaking of what to eat on a sunny day, it's mochi gozen! In Hiraizumi, mochi (rice cakes) is famous as a local dish. Let's have mochi in Hiraizumi and celebrate with Great Fortune! Congratulations!"

    elif fortune == "Good Luck":
        text = "Let's eat Benkei-no-Chikara-Mochi, which has been loved in Hiraizumi for over 105 years, and store your inner energy! You can find it at souvenir shops or the station. The main store is located on Chusonji Street."

    elif fortune == "Fairly Good Luck":
        text = "Hiraizumi, once said to be the second most prosperous city after Kyoto. Let's feel the serene and quiet atmosphere of Hiraizumi, where our hearts can find tranquility. Take a deep breath of Hiraizumi's air and immerse yourself in its essence. Recommended to visit Genbikei Gorge and Mount Kinkeisan."

    elif fortune == "Small Luck":
        text = "Let's visit the spots in Hiraizumi to experience the four seasons. You will surely feel the blissful paradise of Hiraizumi. Recommended to see the view of the Kitakami River and the mountains from Takadate in the summer, as well as the leaf foliage at Motsuji Temple in the fall."

    else:
        text = "Let's gaze at the sunset sinking behind Mount Kinkazan from Muryokoin, one of the World Heritage sites. It will surely purify our hearts. Enjoy the moment!"
    print(fortune)
    return render_template("petit_infoeng.html", fortune=fortune, text=text)


if __name__ == "__main__":
    app.run(port=8002, debug=True)
