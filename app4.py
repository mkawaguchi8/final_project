import random
from flask import Flask, render_template

app = Flask(__name__)


# おみくじアプリルーティング
@app.route(""/omikuji"")
def omikuji():
    # 変数を作成
    rand = random.randint(1, 100)
    omikuji = {
    ""大吉"": 5, 
    ""中吉"": 10, 
    ""吉"": 35, 
    ""凶"": 30, 
    ""大凶"": 20,
    # テンプレートでresult変数を使用する
    return render_template(""omikuji.html"", rand=rand)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
