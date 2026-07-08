## this is a movie library application
# 
# Movies have: title-year-genre
# 
# users can:
#   add a movie
#   see all movies
#   edit a movie
#   delete a movie

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# we create our app
app = Flask(__name__)

# we give the address to our database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
# we disable change tracking, which saves memory
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# we initialize our database!
db = SQLAlchemy(app)

# let's create a model of our Movies
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    # optional: this gives a cleaner debugging representation in Python.
    def __repr__(self):
        return f"<Movie {self.title}>"


# Defining that the model class does not automatically create the real database table.
# here we tell Flask-SQLAlchemy to create the tables.
# Docs explain that many extension operations require an application context.
with app.app_context():
    # actually builds the table in the database if it doesn't exist yet.
    db.create_all() # We do the MAPPING HERE


@app.route("/")
def index():
    movies = Movie.query.all() # get all of the rows in the table
    print(type(movies))
    return render_template("index.html", movies=movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    # if the request from our form is POST:
    if request.method == "POST":
        # get the data from the form
        title = request.form["title"]
        year = request.form["year"]
        genre = request.form["genre"]

        # create the object of Model
        movie = Movie(title=title, year=int(year), genre=genre)

        # add and commit the new entry to the database
        db.session.add(movie) # this is the object that should be inserted
        db.session.commit() # the transaction is finalized!

        # once it's done, go back to the index page
        return redirect(url_for("index"))
    
    return render_template("add_movie.html")

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    # we make a query to find the movie by id
    movie = Movie.query.get_or_404(movie_id)

    if request.method == "POST":
        # change all of the fields to the form
        movie.title = request.form["title"]
        movie.year = int(request.form["year"])
        movie.genre = request.form["genre"]

        # update the database with the changes
        db.session.commit()

        return redirect(url_for("index"))
    
    return render_template("edit_movie.html", movie=movie)


@app.route("/delete/<int:movie_id>")
def delete_movie(movie_id):
    # get the row
    movie = Movie.query.get_or_404(movie_id)
    
    # delete the row
    db.session.delete(movie)

    #finalize transaction
    db.session.commit()

    # go back to main page
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)