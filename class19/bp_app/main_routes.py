from flask import Blueprint, render_template

# create a blueprint named main!
main = Blueprint("main", __name__)

# @main means the routes belong to the blueprint, and not the app directly!
@main.route("/")
def home():
    return render_template("home.html")


@main.route("/about")
def about():
    return render_template("about.html")