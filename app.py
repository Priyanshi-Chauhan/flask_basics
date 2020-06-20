from flask import Flask, render_template, redirect
app = Flask(__name__)  # __name__ is the module name
friends = ["priyanshi", "nokia", "neetu", "mahesh"]
num = 5


@app.route("/")
def hello():
    return render_template("index.html", my_friends=friends, number=num)


@app.route("/terms")
def about():
    return "<h1>about terms<h1>"


@app.route("/policy")
def home():
    return redirect("/")


if __name__ == '__main__':

    app.run(debug=True)
