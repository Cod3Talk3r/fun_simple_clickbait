from flask import Flask, render_template
from random import randint

app = Flask(__name__)

all_clicks = 0


@app.route("/")
def home():
    global all_clicks
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    all_clicks += 1
    color = tuple((r, g, b))

    return render_template("index.html", all_clicks=all_clicks, color=color)


if __name__ == "__main__":
    app.run(debug=True)
