from flask import Flask, render_template
from random import randint
app = Flask(__name__)


quotes = ["quote (c) Mark"]

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/get_quote')
def quote():
    return quotes[randint(0, len(quotes))]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
