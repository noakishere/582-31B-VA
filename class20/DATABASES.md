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
