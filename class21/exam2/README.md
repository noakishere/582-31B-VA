# Advanced Web Programming — Exam 2

## Debugging a Flask Album Catalog

### Duration

3 hours

### Format

Individual debugging exam

### Total

100 marks

---

# Exam overview

You have been given a partially completed Flask application called:

## Independent Album Catalog

The application is intended to manage a small collection of albums.

Users should be able to:

- view all albums
- filter albums by genre
- add a new album
- edit an existing album
- delete an album
- see whether an album is currently in stock

The application already contains most of the necessary code, but many parts are incorrect.

Your task is to:

1. run the application
2. read the errors carefully
3. locate the defects
4. correct the code
5. test every feature
6. document the most important corrections
7. commit your work incrementally with Git

You are not expected to rebuild the application from scratch.

---

# Concepts assessed

This exam assesses concepts covered in class:

- Python classes
- constructors
- instance attributes
- properties
- `__repr__`
- Flask application setup
- routes
- route parameters
- GET and POST requests
- query parameters
- HTML forms
- `request.args`
- `request.form`
- redirects
- `url_for()`
- Jinja templates
- Flask-SQLAlchemy
- ORM models
- database queries
- creating records
- updating records
- deleting records
- database commits
- Git commits and branches
- debugging startup, runtime, and logic errors

---

# Types of errors included

The starter application contains several types of defects:

- syntax errors
- incorrect variable names
- incorrect method calls
- missing parentheses
- incorrect conditions
- incorrect data types
- incorrect route methods
- incorrect form field names
- incorrect template variables
- incorrect route parameter names
- missing database operations
- incorrect redirects
- incorrect model attributes
- logical errors

The starter application contains numerous defects across several files. You are not required to identify a specific number of bugs. Your goal is to make the application satisfy all final requirements.

---

# Repository instructions

Complete this exam inside your existing course repository.

You must make at least four meaningful commits.

Do not use vague messages such as: (will be **penalized**)

```text
fix
changes
final
stuff
```

---

# Project structure

```text
exam2/
│
├── app.py
│
├── static/
│   └── styles.css
│
└── templates/
    ├── base.html
    ├── index.html
    ├── add_album.html
    └── edit_album.html
```

# Required final behaviour

The corrected application must meet all of the following requirements.

## Application startup

- The Flask application starts without a traceback.
- Flask-SQLAlchemy is initialized correctly.
- The SQLite database is created.
- The `album` table is created.

## Album list

- Visiting `/` displays all albums.
- If there are no albums, an empty-state message is displayed.
- Each album displays:
  - title
  - artist
  - genre
  - year
  - stock
  - availability

## Genre filtering

The URL:

```text
/?genre=Electronic
```

must display only albums in the Electronic genre.

Selecting “All genres” must display every album.

## Create

Visiting:

```text
/albums/add
```

must display the create form.

Submitting the form must:

- create an `Album` object
- convert year and stock to integers
- add the object to the database session
- commit the transaction
- redirect to the album list

## Update

Visiting:

```text
/albums/<album_id>/edit
```

must:

- load the correct album
- display its current data in the form

Submitting the form must:

- update the correct attributes
- convert year and stock to integers
- commit the changes
- redirect to the album list

## Delete

Deleting an album must:

- use a POST request
- load the correct album
- delete it from the database session
- commit the deletion
- redirect to the album list

## Templates

- Every template must extend `base.html`.
- Every form field name must match the corresponding backend code.
- Every `url_for()` call must use the correct endpoint.
- Route parameter names must match the route definitions.
- The `in_stock` property must be accessed correctly.

---

# Part 1 — Main debugging application

---

# Starter `app.py`

```python
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///albums.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy


class Album(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(120),
        nullable=False
    )

    artist = db.Column(
        db.String(120),
        nullable=False
    )

    genre = db.Column(
        db.String(80),
        nullable=False
    )

    year = db.Column(
        db.String(4),
        nullable=False
    )

    stock = db.Column(
        db.Integer,
        nullable=False,
        default="0"
    )

    @property
    def in_stock(self):
        return self.stock < 0

    def __repr__(self):
        return self.id


with app.app_context:
    db.create_all()


@app.route("/")
def index():
    genre = request.args.get("category", "")

    if genre:
        albums = Album.query.filter_by(
            artist=genre
        ).all()
    else:
        albums = Album.query.all

    return render_template(
        "index.html",
        album=albums,
        selected_genre=genre
    )


@app.route(
    "/albums/add",
    methods=["GET"]
)
def add_album():
    if request.method == "POST":
        album = Album(
            title=request.form["album_name"],
            artist=request.form["artist"],
            genre=request.form["genre"],
            year=request.form["year"],
            stock=request.form["stock"]
        )

        db.session.commit()

        return redirect(
            url_for("albums")
        )

    return render_template(
        "add_album.html"
    )


@app.route(
    "/albums/<int:album_id>/edit",
    methods=["GET", "POST"]
)
def edit_album(album_id):
    album = Album.query.get_or_404(album_id)

    if request.method == "POST":
        album.title = request.form["title"]
        album.band = request.form["artist"]
        album.genre = request.form["genre"]
        album.year = request.form["year"]
        album.stock = request.form["amount"]

        return redirect(
            url_for(
                "edit_album",
                id=album.id
            )
        )

    return render_template(
        "add_album.html",
        album=album
    )


@app.route(
    "/albums/<int:album_id>/delete",
    methods=["GET"]
)
def delete_album(album_id):
    album = Album.query.get_or_404(album_id)

    db.session.delete(album)

    return redirect(
        url_for("index")
    )


if __name__ == "__main__":
    app.run(debug=True)
```

---

# Starter `templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />

    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>{% block title %} Independent Album Catalog {% endblock %}</title>

    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='styles.css') }}"
    />
  </head>

  <body>
    <header class="site-header">
      <h1>Independent Album Catalog</h1>

      <nav>
        <a href="{{ url_for('albums') }}"> All Albums </a>

        <a href="{{ url_for('add') }}"> Add Album </a>
      </nav>
    </header>

    <main class="container">{% block content %} {% endblock %}</main>
  </body>
</html>
```

---

# Starter `templates/index.html`

```html
{% extends "base.html" %} {% block title %} Album Catalog {% endblock %} {%
block content %}

<h2>Albums</h2>

<form method="GET" action="{{ url_for('index') }}">
  <label for="genre"> Filter by genre </label>

  <select id="genre" name="category">
    <option value="">All genres</option>
    <option value="Electronic">Electronic</option>
    <option value="Rock">Rock</option>
    <option value="Hip-Hop">Hip-Hop</option>
    <option value="Experimental">Experimental</option>
  </select>

  <button type="submit">Filter</button>
</form>

<p>
  <a href="{{ url_for('add_album') }}"> Add an album </a>
</p>

{% if album %}

<div class="album-grid">
  {% for item in albums %}

  <article class="album-card">
    <h3>{{ item.name }}</h3>

    <p>
      <strong>Artist:</strong>
      {{ item.band }}
    </p>

    <p>
      <strong>Genre:</strong>
      {{ item.genre }}
    </p>

    <p>
      <strong>Year:</strong>
      {{ item.year }}
    </p>

    <p>
      <strong>Stock:</strong>
      {{ item.stock }}
    </p>

    <p>
      <strong>Availability:</strong>

      {% if item.in_stock() %} In stock {% else %} Sold out {% endif %}
    </p>

    <a
      href="{{ url_for(
                        'edit_album',
                        id=item.id
                    ) }}"
    >
      Edit
    </a>

    <a
      href="{{ url_for(
                        'delete_album',
                        album_id=item.id
                    ) }}"
    >
      Delete
    </a>
  </article>

  {% endfor %}
</div>

{% else %}

<p>No albums have been added.</p>

{% endif %} {% endblock %}
```

---

# Starter `templates/add_album.html`

```html
{% extends "base.html" %} {% block title %} Add Album {% endblock %} {% block
content %}

<h2>Add Album</h2>

<form method="GET" action="{{ url_for('add_album') }}">
  <p>
    <label for="title">Title</label>

    <input id="title" name="title" type="text" required />
  </p>

  <p>
    <label for="artist">Artist</label>

    <input id="artist" name="artist" type="text" required />
  </p>

  <p>
    <label for="genre">Genre</label>

    <select id="genre" name="genre" required>
      <option value="">Choose a genre</option>
      <option value="Electronic">Electronic</option>
      <option value="Rock">Rock</option>
      <option value="Hip-Hop">Hip-Hop</option>
      <option value="Experimental">Experimental</option>
    </select>
  </p>

  <p>
    <label for="year">Year</label>

    <input id="year" name="year" type="number" required />
  </p>

  <p>
    <label for="stock">Stock</label>

    <input id="stock" name="stock" type="number" min="0" required />
  </p>

  <button type="submit">Save Album</button>
</form>

<p>
  <a href="{{ url_for('index') }}"> Cancel </a>
</p>

{% endblock %}
```

---

# Starter `templates/edit_album.html`

```html
{% extends "base.html" %} {% block title %} Edit Album {% endblock %} {% block
content %}

<h2>Edit Album</h2>

<form
  method="POST"
  action="{{ url_for(
        'edit_album',
        album_id=album.id
    ) }}"
>
  <p>
    <label for="title">Title</label>

    <input
      id="title"
      name="title"
      type="text"
      value="{{ album.name }}"
      required
    />
  </p>

  <p>
    <label for="artist">Artist</label>

    <input
      id="artist"
      name="artist"
      type="text"
      value="{{ album.band }}"
      required
    />
  </p>

  <p>
    <label for="genre">Genre</label>

    <input
      id="genre"
      name="genre"
      type="text"
      value="{{ album.genre }}"
      required
    />
  </p>

  <p>
    <label for="year">Year</label>

    <input
      id="year"
      name="year"
      type="number"
      value="{{ album.year }}"
      required
    />
  </p>

  <p>
    <label for="stock">Stock</label>

    <input
      id="stock"
      name="quantity"
      type="number"
      min="0"
      value="{{ album.stock }}"
      required
    />
  </p>

  <button type="submit">Update Album</button>
</form>

<p>
  <a href="{{ url_for('index') }}"> Cancel </a>
</p>

{% endblock %}
```

---

# Starter `static/styles.css`

```css
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f4f1ec;
  color: #222;
}

.site-header {
  padding: 1rem 2rem;
  background: #202020;
  color: white;
}

.site-header a {
  margin-right: 1rem;
  color: white;
}

.container {
  width: min(1000px, 92%);
  margin: 2rem auto;
}

.album-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 1rem;
}

.album-card {
  padding: 1rem;
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
}

form {
  margin-block: 1rem;
}

input,
select,
button {
  padding: 0.5rem;
}
```

# Part 2 — Debugging explanation

## 10 marks

Create a file named:

```text
DEBUGGING_REPORT.md
```

Document five important bugs you corrected.

For each bug, include:

```markdown
## Bug title

**File:**  
Name of the file.

**Problem:**  
What was incorrect?

**Fix:**  
What did you change?

**Test:**  
How did you confirm that it worked?
```

At least one example must come from each of these categories:

- Python or model code
- Flask route
- database operation
- template or form
- logic error

---

# Suggested debugging order

## Warning:

**Database reset note**: This exam does not use migrations. During debugging, you may stop Flask, delete instance/albums.db, and restart the application to recreate the database after correcting the model. The starter database contains no required data.

## Stage 1 — Start the application

First examine:

- Flask-SQLAlchemy configuration
- `SQLAlchemy` initialization
- application context
- model syntax and data types

Do not begin with the templates if Flask cannot start.

## Stage 2 — Display albums

Test the `/` route.

Check:

- the query
- .all()
- template variable names
- model attribute names
- property access

## Stage 3 — Test filtering

Test:

```text
/?genre=Electronic
```

Check:

- the query parameter name
- the model field being filtered

## Stage 4 — Test adding

Check:

- route methods
- form method
- form field names
- integer conversion
- `db.session.add()`
- `db.session.commit()`
- redirect endpoint

## Stage 5 — Test editing

Check:

- model attribute names
- form field names
- number conversion
- template name
- database commit
- redirect parameters

## Stage 6 — Test deleting

Check:

- GET versus POST
- HTML form versus link
- `db.session.delete()`
- `db.session.commit()`

---

# Final acceptance checklist

Before submitting, confirm:

- [ ] Flask starts without an error.
- [ ] The database and table are created.
- [ ] `/` displays all albums.
- [ ] The empty-state message works.
- [ ] Filtering by genre works.
- [ ] The add form uses POST.
- [ ] Adding an album works.
- [ ] Year is stored as an integer.
- [ ] Stock is stored as an integer.
- [ ] The new album remains after restarting Flask.
- [ ] The edit form displays current album values.
- [ ] Editing an album works.
- [ ] Edited data remains after restarting Flask.
- [ ] The `in_stock` property works.
- [ ] Deletion uses POST.
- [ ] Deleting an album works.
- [ ] All links and forms use valid endpoints.
- [ ] All route parameter names are correct.
- [ ] The debugging report contains five bugs.
- [ ] Git contains at least four meaningful commits.

---

# Grading rubric

## 1. Flask startup and SQLAlchemy setup — 15 marks

- correct configuration key
- correct SQLAlchemy initialization
- correct application context
- database table creation

## 2. Album model — 15 marks

- correct column types
- correct default value
- correct `in_stock` property
- correct `__repr__`

## 3. List and filtering — 15 marks

- correct query parameter
- correct filtering field
- correct `.all()` call
- correct template variable

## 4. Create operation — 15 marks

- correct route methods
- correct form method
- matching field names
- integer conversion
- session add
- commit and redirect

## 5. Edit operation — 15 marks

- correct object lookup
- correct attributes
- matching form names
- correct conversions
- correct template
- commit and redirect

## 6. Delete operation — 10 marks

- POST request
- correct object lookup
- session delete
- commit
- redirect

## 7. Debugging report and Git — 15 marks

- useful report
- meaningful commit history

### Total: 100 marks

---

# Important exam note

This exam does not require students to introduce unfamiliar Flask architecture.

Students should fix the existing code using the same patterns practiced during lectures and lab:

```python
app = Flask(__name__)
db = SQLAlchemy(app)
```

```python
Model.query.all()
```

```python
db.session.add(object)
db.session.commit()
```

```python
db.session.delete(object)
db.session.commit()
```

```python
request.form["field_name"]
```

```python
return redirect(url_for("route_name"))
```

The challenge comes from reading, tracing, and correcting code.

Good luck!
