from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import (check_password_hash, generate_password_hash)

# let's start our db
db = SQLAlchemy()

# Now create the model class
# why do we inherit from UserMixin
#                                   Flask-login expects user objects to provide properties and methods such as:
#                                       is_authenticated, is_active, is_anonymous, etc.
#                                   UserMixin supplies reasonable default implementations.
class Member(UserMixin, db.Model):
    __tablename__ = "member"

    #let's define our fields
    id = db.Column(db.Integer,
                   primary_key=True)
    
    username = db.Column(db.String(50),
                         nullable=False,
                         unique=True)
    
    email = db.Column(db.String(255),
                      nullable=False,
                      unique=True)
    
    password_hash = db.Column(db.String(255),
                              nullable=False)
    
    # methods
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    #log
    def __repr__(self):
        return(f"<Member {self.id}: {self.username}")