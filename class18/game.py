from flask import Flask 

app = Flask(__name__)  

# we want an app with 3 routes
#   /  
#   /games
#       make it to return an HTML unordered list with 3 game names.
#   /students
# each route should return different HTML content.

@app.route("/")
def hello():
    return "Hello to my website"

@app.route("/games")
def games():
    games_list = ""

    for i in range(1,4):
        games_list += f"<li>Game {i}</li>"

    return f"""
    <h1>Games List:</h1>
    <ul>{games_list}</ul>
    """
    # return "<ul><li>Game 1</li><li>Game 2</li><li>Game 3</li></ul>"

@app.route("/students")
def students():
    return "welcome to students page"

