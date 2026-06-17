# =================================================
# What is templating?

# Flask uses Jinja templates for rendering HTML, and you should note that Jinja
# autoescapes rendered user input in HTML by default.

# Why templates?

# Templates allow:

#   1. cleaner HTML files
#   2. dynamic placeholders
#   3. loops and conditionals
#   4. separation between Python logic and page structure.

from flask import Flask, render_template, request # import render_template

app = Flask(__name__)

@app.route("/")
def home():
    # render_template tells Flask to render an HTML template
    return render_template("home.html", title="Welcome", message="Hello from" \
    " flask templates!")
    # ^^^^^^^^^ title and message are passed from Python into the template
    # inside the HTML file {{ variable_name }} outputs values in Jinja templates

@app.route("/games")
def games():
    # prepare the list
    games_list = ["Street fighter", "Tetris", "Pac-Man"]

    # send the list as a parameter
    return render_template("games.html", games=games_list)

# ==============================================================
# looking at request data

@app.route("/greet")
def greet():
    # fLask can read name from the request
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name} </h1>"

@app.route("/welcome")
def welcome():
    name = request.args.get("name", "Guest")
    program = request.args.get("program", "Unknown")
    return f"<h1>{name} studies in the {program} program.</h1>"