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



# common mistakes to watch for:

#   1. Never forget to register the blueprint!
#   2. don't mix @app.route and @blueprint.route
#   3. Dont forget the imports!!
#   4. BLUEPRINTS ARE NOTTTT SEPARATE APPLICATIONS
#       BPs are sections of one application!
#       the app object ties everything together!


