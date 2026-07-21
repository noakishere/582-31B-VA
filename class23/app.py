import os
from dotenv import load_dotenv
from flask import (Flask, flash, redirect, render_template, request, url_for)
from flask_login import (LoginManager, current_user, login_required, login_user, logout_user)


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ("sqlite:///foundry.db")

# Flask uses the secret key to securely sign sesssion information and flash messages.
# Without, login sessions and flash messages cannot function properly.
# In a deployed application (whether final or dev) the secret should come from an envrionment variable.
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# db


# login
login_manager = LoginManager()
login_manager.login_view = "login"

login_manager.init_app(app)
