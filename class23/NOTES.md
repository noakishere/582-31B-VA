## Authentication and user accounts in Flask

### Authentication vs Authorization

Authentication means : is the user logged in?

Authorization means: is the user allowed to do an action. (edit, view, etc.)

### Terminology

- Password hashing: A one-way representation of a password. (to hide)

- Session: Data used to remember a user between requests
  - a temporary, server-side record of a user's interaction with a website.

- Protected route: A route that requires authentication

- Flash message: A temporary message displayed after an action (usually, a request)

- Unique constraint: A database rule preventing duplicate values.

- Credential: Information used to prove identity.

### Example

Request 1: POST /login

--> Credentials verified (username, password is verified!)

--> User ID is stored in session

--> Request 2: GET /dashboard

--> Session identifies the member (member associated with the content)

--> current_user (from session) contains the member ,etc. etc.

### Passwords and why they shouldn't be stored dircetly

When the user registers, if we store their password directly in the database (like Password123 for example), in case of a database exposure or exploit, every password becomes immediatebly readable.

We want to store a password hash:

i.e.: Password 123 --> scrypt:3247574279:8.1$ (not real)

A hash is designed to be one-way. The application cannot decrypt it.

Instead, it asks: does the submitted password (let's say in the login page) produce a matching result. (when hashing)

- **Register Process** is: Plain Passowrd --> generate_password_hash() --> Password hash --> database

- **Login Process** is: Submitted Plain Password --> check_password_hash() --> True or False
