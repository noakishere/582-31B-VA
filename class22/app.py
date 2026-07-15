from flask import (Flask, render_template, request, redirect, url_for)


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bikes.db"

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

# bidirectional relationship
# Station.bikes <--> Bike.station
    

# Define every model before calling db.create_all()!!!!
with app.app_context():
    db.create_all()

    downtown_station = Station(
        name="Downtown Station",
        capacity=4
    )

    bike_100 = Bike(
        bike_type="Standard",
        is_available=True,
        distance_km=200
    )

    bike_101 = Bike(
        bike_type="Electric",
        is_available=True,
        distance_km=800
    )

    bike_102 = Bike(
        bike_type="Electric",
        is_available=True,
        distance_km=1000
    )

    # ^ These bikes dont have stations yet!!


    # To connect:
    # through relationships
    # adds it to bikes, and with back_populate, also assigns the station field on the bike

    # Option 1:
    downtown_station.bikes.append(bike_100)
    downtown_station.bikes.append(bike_101)

    # Option 2:
    bike_102.station = downtown_station

    # We can see the objects!

    # Let's not forget to add and commit!
    db.session.add(downtown_station)
    db.session.commit()

    db.session.add(bike_100)
    db.session.add(bike_101)
    db.session.add(bike_102)

    db.session.commit()

    print(downtown_station.bikes)
    print(bike_102.station)