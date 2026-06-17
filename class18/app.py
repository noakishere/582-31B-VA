# The core loop of backend:
# The browser displays the interface
# the bakcend receives requests
# the backend decides what data or page to send back
# the backend may validate input, apply business rules, talk to a database, 
#   render templates, and return a response.

# IMPORTANT: never name your file flask.py

from flask import Flask # import flask

app = Flask(__name__) # create the application object. 
# __name__ is commonly used here so Flask knows where to look for resources.

# associate the URL path  with the function below.
# this decorator tells Flask what URL should trigger the function.
@app.route("/")
def hello():
    # returns the response sent to the browser.
    return "<h1>Home Page</h1> <p>Welcome to my website.</p>" 

@app.route("/about")
def about():
    name = "Jane"
    return f"<h1>About</h1> <p>This is the about page for {name}.</p>"

@app.route("/contact")
def contact():
    return "<h1>Contact</h1> <p>Contact us here.</p>"

# Request-response cycle :

#   1. browser requests a URL
#   2. Flask receives the request
#   3. Flask matches a route
#   4. Python function runs
#   5. response is returned.