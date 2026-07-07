from flask import Flask
from main_routes import main
from team_routes import teams

app = Flask(__name__)
# tell the main Flask app to include those routes!
app.register_blueprint(main)
app.register_blueprint(teams)

# file structure:
# bp_app/
#   app.py
#   main_routes.py
#   templates/
#       home.html
#       about.html

