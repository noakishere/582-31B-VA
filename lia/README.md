# LIA

For this Learning Integration Assessment, your task is to build a small Flask application called **Shelf**.

Shelf is a personal reading-list application where registered users can save books they want to read.

The application must use:

- Flask
- Flask-SQLAlchemy
- Flask-Login
- Jinja templates
- a SQLite database

## Requirements

- Users can create an account with:
  - a unique username
  - a unique email address
  - a password

- Passwords must be stored securely using password hashing.

- Users can log in and log out.

- Only logged-in users can access their reading list.

- Logged-in users can add a book to their reading list.

- A book contains:
  - a title
  - an author
  - an optional note
  - a reading status

- The reading status must be one of:
  - `Want to read`
  - `Reading`
  - `Finished`

- A title:
  - may not be blank
  - may contain up to 100 characters

- An author:
  - may not be blank
  - may contain up to 100 characters

- A note:
  - is optional
  - may contain up to 1,000 characters

- Users can view all the books in their own reading list.

- Users must not be able to view another user's reading list.

- Users can update the reading status of one of their books.

- Users can delete one of their books.

- Users must not be able to update or delete books that belong to another account.

- The navigation changes depending on authentication state:
  - logged-out users see links to register and log in
  - logged-in users see links to their reading list and log out

- Flash messages are displayed when users:
  - create an account
  - log in
  - log out
  - add a book
  - update a book
  - delete a book

## Suggested models

Your application should contain two models:

```text
User
Book
```

Their relationship is:

```text
User 1 ──────── * Book
```

This means:

- one user can have many books
- each book belongs to one user

Your exact field and relationship names are your design decision, but they must be clear and consistent.

## Suggested routes

Your route names may differ, but the application will likely need routes serving these purposes:

```text
GET, POST  /register
GET, POST  /login
POST       /logout

GET         /books
GET, POST   /books/new
GET, POST   /books/<book_id>/edit
POST        /books/<book_id>/delete
```

## Authentication guidance

You may use the following Flask-Login tools:

```python
LoginManager
UserMixin
login_user
logout_user
current_user
login_required
```

The user model should provide methods for setting and checking passwords.

For example:

```python
user.set_password(password)
user.check_password(password)
```

Do not store plain-text passwords.

## Ownership guidance

Every book must belong to the user who created it.

When creating a book, use the currently logged-in user rather than asking the user to select an owner.

Before updating or deleting a book, verify that the book belongs to `current_user`.

An authenticated user must not be able to modify another user's data by manually changing the URL.

## Validation guidance

Use browser-side validation where appropriate:

```html
required maxlength
```

Important rules must also be validated on the server.

The application should handle invalid input without crashing.

## Suggested project structure

```text
shelf/
│
├── app.py
├── models.py
├── requirements.txt
├── README.md
│
├── static/
│   └── styles.css
│
└── templates/
    ├── base.html
    ├── register.html
    ├── login.html
    ├── books.html
    ├── book_form.html
    └── book_edit.html
```

A different structure is acceptable if it is clear and organized.

## Assessment criteria

### Program design [5]

- requirements are met
- Flask routes are decomposed into manageable, logical pieces
- models and relationships are appropriate
- authentication is implemented correctly
- passwords are securely hashed
- protected routes require authentication
- users may only access their own data
- validation is handled correctly
- common code is unified, not duplicated
- templates, routes, and models have separate responsibilities
- markup is semantic
- no unnecessary global variables

### Readability [3]

- constants are used instead of unexplained hard-coded values
- complex or meaningful expressions are named
- naming is consistent and descriptive
- comments explain reasoning
- documentation explains important public interfaces
- code is formatted consistently
- templates are readable and organized

### Version control [2]

- commits contain related changes
- commit messages are consistent and informative
- development history shows meaningful progress

## Recommended implementation order

1. Create the Flask application and database.
2. Create the `User` model.
3. Add password hashing.
4. Implement registration.
5. Implement login and logout.
6. Create the `Book` model and relationship.
7. Display the current user's books.
8. Add book creation.
9. Add book editing.
10. Add book deletion.
11. Add ownership checks.
12. Add flash messages and final styling.
