from flask import Flask, render_template

app = Flask(__name__)

i = 0


@app.route("/")
def home():
    global i
    i += 1

    return render_template("index.html", i=i)


if __name__ == "__main__":
    app.run(debug=True)