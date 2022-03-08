from flask import Flask, render_template, request

# create an instance of flask object
app = Flask(__name__)


def index():
    return render_template("layouts/index.html")


if __name__ == "__main__":
    app.run(debug=True)