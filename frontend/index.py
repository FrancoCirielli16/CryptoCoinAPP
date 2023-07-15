from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def principal():
    return render_template("index.html")

@app.route('/cryptos')
def cryptos():
    return render_template("cryptos.html")

@app.route('/profile')
def subs():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True, port=1605)