from flask import Flask, render_template, redirect
app = Flask(__name__)  # __name__ is the module name
friends = ["priyanshi", "priyanka", "neetu", "mahesh"]


@app.route("/")
def hello():
    return render_template("index.html", my_friends=friends)


@app.route("/about")
def about():
    return "<h1>about page<h1>"


@app.route("/home")
def home():
    return redirect("/")


if __name__ == '__main__':

    app.run(debug=True)
