# Databases

### Database vs DBMS

A **database** is the stored data itself.
A **DBMS** is the software that manages that data.

### What is a database?

A database is an organized collection of data.

### What is a DBMS?

A DBMS is a Database Managament System.

Examples of DBMSs:

- SQLite
- PostgreSQL
- MySQL

### What is an ORM?

An ORM is an Object Relational Mapper.

If our relational database has:

- tables
- rows
- columns

Python on the other hand has:

- classes
- objects
- attributes

**_ORM maps these two worlds._**

- tables <-> classes
- rows <-> objects
- columns <-> attributes

### What is SQLAlchemy?

SQLAlchemy describes itself as a toolkit plus ORM for working with databases and Python.

### Clear mapping example

#### Database View

Table:movie

id | title | year

1 | inception | 2010

2 | Interstellar | 2014

#### Python ORM view

class Movie:
id:int
title: str
year: int

### GET vs POST

#### GET

What display the form!

#### POST

What processes the submitted form data.

#### Request Flow

1. browser vists /add (for example)
2. Flask renders the form
3. user submits the form (with the submit button)
4. Flask reads the submitted fields from request.form
5. Flask constructs a Movie(model) object (for example)
6. Flask adds it to the session
7. Flask commits it to the database.
8. Flask redirects back to the homepage (or whatever you want to happen)

## Some notes

### Model definition

The model class is not only a normal Python class. It is, in addition to that, a description of a database table.

### add() and commit()

- `add()` tells SQLAlchemy which new object should be inserted.
- `commit()` finalizes the transaction (applies the changes to DB).

### Persistance

With a database, now browser actions change persistent data.

## What is a session???

The session is the ORM unit that tracks objects (python) and coordinates the transaction. SQLAlchemy docs emphasize that the session is stateful and _transaction-oriented_.
