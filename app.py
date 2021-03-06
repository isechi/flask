from flask import Flask , render_template
# flaskのflask,render,templateを使用します宣言
app = Flask(__name__)

@app.route("/test")
def test():
    name = "flask"
    return render_template("test.html",name = name)

@app.route("/greet/<text>")
def hello(text):
    return text + "さん、こんにちは"


if __name__ == "__main__":
    # サーバーを起動するよ
    app.run(debug=True)
    # デバッグモードを有効にするよ（使いたくない場合はFalse)