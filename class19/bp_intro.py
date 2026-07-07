from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "test"

# let's say my application has 7 pages!

# a bigger app should be divided by responsibility!
#           to do this idea, we can use blueprints!


# A blueprint is a way to group related routes together!

#   main page in one bp
#   matches in another
#   players page in another
#   etc..



