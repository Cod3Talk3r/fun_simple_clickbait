from flask import Flask, render_template
from random import randint

app = Flask(__name__)

i = 0


@app.route("/")
def home():
    global i
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    i += 1
    color = tuple((r, g, b))

    return render_template("index.html", i=i, color=color)


if __name__ == "__main__":
    app.run(debug=True)
