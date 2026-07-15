from flask import (Flask, render_template, request, redirect, url_for)


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://bikes.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Let's define the Station model
# the station has --> id, name, capacity
class Station(db.Model):
    # let's give it a table name!
    # this same name will be used in the foreign key!
    # station.id
    # !!!Foreign Key uses the table name, not the Python class name!!!
    __tablename__ = "station"

    id = db.Column(db.Integer,
                   primary_key=True)
    
    name = db.Column(db.String(120),
                     nullable=False)
    
    capacity = db.Column(db.Integer,
                         nullable=False)
    
    bikes = db.relationship(
        "Bike",
        back_populates="station" #refers to Bike.station
    )
    
    def __repr__(self):
        return (
            f"<Station {self.id}: {self.name}>"
        )
    
class Bike(db.Model):
    __tablename__ = "bike"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    bike_type = db.Column(
        db.String(50),
        nullable=False
    )
    
    is_available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    distance_km = db.Column(
        db.Float,
        nullable=False,
        default=0
    )

    station_id = db.Column(
        db.Integer,
        db.ForeignKey("station.id"), #uses the tablename.id , not Python class name!
        nullable=False
    )

    station = db.relationship(
        "Station",
        # SQLAlchemy uses matching back_populates values to connect both sides of a bidirectional rel.
        back_populates="bikes" #refers to the attribute on Station.bikes
    )

    def __repr__(self):
        return (
            f"<Bike {self.id}: {self.bike_type}>"
        )
    


# Station.bikes <--> Bike.station