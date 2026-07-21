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


#### Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    # if authenticated, you can't register!
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    
    if request.method == "POST":
        "     t_rex        "
        username = request.form["username"].strip()

        email = request.form["email"].strip().lower()

        password = request.form["password"]

        errors = []

        if not username:
            errors.append("Username is required")

        if len(username) > 50:
            errors.append("Username may contain at most 50 characters.")
        
        "t rex"
        if any(character.isspace() for character in username):
            errors.append("Username may not contain whitespace")

        existing_username = Member.query.filter_by(username=username).first()

        if existing_username:
            errors.append("That username is already in use!")

        existing_email = Member.query.filter_by(email=email).first()

        if existing_email:
            errors.append("That email is already registered.")

        password_error = validate_password(password)

        if password_error:
            errors.append(password_error)

        if errors:
            for error in errors:
                flash(error, "error")

            return render_template("register.html", username=username, email=email)
        
        # if no errors!!!
        member = Member(username=username, email=email)

        # hash the password
        member.set_password(password)

        # add it to the table
        db.session.add(member)
        db.session.commit()

        flash("Your account has been created!!!", "success")

        return redirect(url_for("login"))
    
    return render_template("register.html")