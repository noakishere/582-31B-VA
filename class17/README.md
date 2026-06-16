# Advanced Programming — Lab

## Modules and Package Organization with Git

### Duration

3 hours

### Format

Guided VCS refactor lab

---

# Objective

In this lab, you will reorganize a small Python application from a single-file program into a cleaner multi-file project.

You will practice:

- modules
- package-style organization
- imports
- responsibility-based file structure
- Git commits during refactoring
- using a branch for structural changes

The goal is not to build a large new application.
The goal is to **improve structure while keeping the program working**.

---

# Learning Goals

By the end of this lab, you should be able to:

- explain what a module is
- split Python code across multiple files
- organize related code by responsibility
- import classes, constants, enums, and exceptions correctly
- explain what a package-style structure is
- use Git to track refactoring steps
- create and merge a feature branch
- preserve working behavior during code reorganization

---

# Lab Theme

## Movie Booking Refactor

You are given a small single-file Python application for a movie booking system.

Your job is to refactor it into a cleaner modular project using Git to track each major step.

---

# Starter Code

Create a file called:

```text
app.py
```

Paste this starter code into it:

```python id="81001"
from enum import Enum

MAX_TICKETS_PER_BOOKING = 6

class ShowStatus(Enum):
    OPEN = "open"
    SOLD_OUT = "sold_out"
    CANCELLED = "cancelled"

class InvalidBookingError(Exception):
    pass

class Customer:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Customer: {self.name}")

class MovieShow:
    def __init__(self, title, capacity, status):
        self.title = title
        self.capacity = capacity
        self.status = status

    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value}")

def main():
    customer = Customer("Ava")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)

    customer.display_info()
    show.display_info()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)

if __name__ == "__main__":
    main()
```

# Part 1 — Run the Starter Program

Before refactoring, run the program and confirm that it works.

### Expected behavior

It should print:

- customer information
- movie show information
- the maximum tickets constant

You should always know whether the program still works after each refactor step.

---

# Part 2 — Identify the Responsibilities

Look at the starter file and identify these parts:

- constant
- enum
- custom exception
- `Customer` class
- `MovieShow` class
- application entry point (`main()`)

Think about these questions:

1. What is mixed together in this file?
2. Which parts belong together conceptually?
3. Which parts should be moved into separate modules?

---

# Part 3 — Extract Constants, Enum, and Exception

Create these files:

- `constants.py`
- `enums.py`
- `exceptions.py`

## Move the code into the correct files

### `constants.py`

```python id="81003"
MAX_TICKETS_PER_BOOKING = 6
```

### `enums.py`

```python id="81004"
from enum import Enum

class ShowStatus(Enum):
    OPEN = "open"
    SOLD_OUT = "sold_out"
    CANCELLED = "cancelled"
```

### `exceptions.py`

```python id="81005"
class InvalidBookingError(Exception):
    pass
```

Now update your main program file so it imports these values instead of defining them inside the same file.

---

## Required Git step

Commit after this change.

---

# Part 4 — Move Classes into Separate Modules

Create these files:

- `customer.py`
- `movie_show.py`

Move the class definitions out of the original file and into the correct modules.

### `customer.py`

```python id="81006"
class Customer:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Customer: {self.name}")
```

### `movie_show.py`

```python id="81007"
from enums import ShowStatus

class MovieShow:
    def __init__(self, title, capacity, status):
        self.title = title
        self.capacity = capacity
        self.status = status

    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value}")
```

---

## Create a new main file

You may now rename your entry-point file to:

```text
main.py
```

Example:

```python id="81008"
from constants import MAX_TICKETS_PER_BOOKING
from enums import ShowStatus
from customer import Customer
from movie_show import MovieShow

def main():
    customer = Customer("Ava")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)

    customer.display_info()
    show.display_info()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)

if __name__ == "__main__":
    main()
```

Run the program again and confirm it still works.

---

## Required Git step

Commit after this change.

---

# Part 5 — Create a Feature Branch for Package-Style Organization

Now you will practice organizing the project further using a Git branch.

Create a new branch:

```bash id="81009"
git checkout -b feature/package-structure
```

On this branch, reorganize the project into folders.

---

# Target Structure

Refactor your project so it looks like this:

```text
movie_booking/
    main.py
    models/
        customer.py
        movie_show.py
    core/
        constants.py
        enums.py
        exceptions.py
```

You may create the folders:

- `models`
- `core`

Then move the files into the correct folders.

---

# Update Imports

After moving files, update your imports.

For example, `main.py` may now look like this:

```python id="81010"
from core.constants import MAX_TICKETS_PER_BOOKING
from core.enums import ShowStatus
from models.customer import Customer
from models.movie_show import MovieShow

def main():
    customer = Customer("Ava")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)

    customer.display_info()
    show.display_info()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)

if __name__ == "__main__":
    main()
```

You will also need to update imports inside files such as `movie_show.py`.

---

## Required Git step

Commit after this reorganization.

---

# Part 6 — Merge Back into Main

After your branch version is working:

1. switch back to `main`
2. merge the branch into `main`

### Suggested commands

```bash id="81011"
git checkout main
git merge feature/package-structure
```

---

# Part 7 — Final Verification

After merging, verify that:

- the program still runs
- all imports work
- the behavior is unchanged
- your Git history shows meaningful steps

---

# Commands You Should Use

## Run the program

```bash id="81012"
python main.py
```

## Check status

```bash id="81013"
git status
```

## View branch list

```bash id="81014"
git branch
```

## View Git history

```bash id="81015"
git log --oneline --graph --all
```

---

# Required Deliverables

Submit:

- the complete project folder
- the Git repository history intact
- a screenshot or pasted output of:

```bash id="81016"
git log --oneline --graph --all
```

You may also be asked to include:

- a screenshot of the program output

If your instructor requests GitHub, also submit:

- your repository link

---

# Minimum Required Project Evolution

Your Git history should clearly show these stages:

1. starter single-file application
2. constants/enum/exception moved into modules
3. classes moved into separate modules
4. branch created for package-style structure
5. package-style structure merged back into `main`

Do **not** do the whole refactor in one commit.

---

# Challenge Tasks

Complete at least **one** if you finish early.

## Challenge 1 — Add a `Staff` model

Create a new file:

```text
models/staff.py
```

Add a simple `Staff` class and use it in `main.py`.

Commit this change separately.

### Suggested commit message

```text
Add staff model and use it in main
```

---

## Challenge 2 — Add a `utils.py` module

Create a file for helper logic such as display helpers or formatting.

Use it in `main.py`.

---

## Challenge 3 — Add package markers

If your environment uses them, add `__init__.py` files in:

- `models`
- `core`

Then discuss what these package files mean.

---

## Challenge 4 — Create a second feature branch

Create another feature branch for one small improvement, such as:

- adding a new class
- improving display output
- adding another constant

Then merge it back.

---

# Things to Watch Out For

## 1. Refactor in small steps

Do not move everything at once and only test at the end.

A better workflow is:

- make one structural change
- run the program
- commit
- continue

---

## 2. Update imports carefully

After moving files into folders, your old imports may stop working.

Check:

- import paths in `main.py`
- import paths inside model files

---

## 3. Commit after each meaningful change

This is a VCS lab.

Do not make one giant commit at the end.

Good commits reflect clear structural progress.

---

## 4. Use clear commit messages

Bad examples:

- `update`
- `changes`
- `fix`
- `stuff`

Better examples:

- `Extract constant enum and exception into modules`
- `Move customer and movie show classes into separate modules`
- `Reorganize project into models and core folders`

---

## 5. Keep organization reasonable

The goal is cleaner structure, not maximum fragmentation.

Group files by responsibility.
