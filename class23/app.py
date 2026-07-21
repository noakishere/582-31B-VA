import os
from dotenv import load_dotenv

from flask import (Flask, flash, redirect, render_template, request, url_for)
from flask_login import (LoginManager, current_user, login_required, login_user, logout_user)

from models import db, Member

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ("sqlite:///foundry.db")

# Flask uses the secret key to securely sign sesssion information and flash messages.
# Without, login sessions and flash messages cannot function properly.
# In a deployed application (whether final or dev) the secret should come from an envrionment variable.
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# db
db.init_app(app)

# login
login_manager = LoginManager()
login_manager.login_view = "login"

login_manager.init_app(app)

with app.app_context():
    # create the tables
    db.create_all()

#### Loading User
# Let's say:
# session contains: "4"
# user_loader receives "4"
# Database query returns: Member object with ID 4
# current_user becomes: that Member object
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Member, int(user_id))

#### Registeration Validation
def validate_password(password):
    # password: between 8 and 20 chars
    if len(password) < 8:
        return("Password must contain at least 8 characters.")
    
    if len(password) > 20:
        return("Password must contain at most 20 characters.")
    
    # must have one uppercase at least
    if not any(character.isupper() for character in password):
        return("Password must contain at least an uppercase letter.")
    
    # password must have a number in it
    if not any(character.isdigit() for character in password):
        return("Password must contain a digit.")
    
    # This means password is valid
    return None

# for example:
# password_error = validate_password("gjlksgjfs")
# if password_error:
#     flash(password_error, "error")

