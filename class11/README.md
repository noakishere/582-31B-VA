# Advanced Programming — Async Session

## Enums and Constants in Application Design

### Format

Self-paced lab-lecture

### Estimated time

3 hours

# Objective

In this session, you will learn how to represent fixed sets of allowed values in Python using:

- constants
- `Enum`
- validation with enums
- enums inside class design

You will then apply these ideas in a small guided lab.

This lesson connects directly to the last sessions on:

- encapsulation
- properties
- validation
- invariants

because enums help classes accept only valid values from a known set.

---

# Learning Goals

By the end of this session, you should be able to:

- explain what a constant is
- explain what an enum is
- distinguish constants from enums
- use Python’s `Enum` class
- access enum members correctly
- compare enum values
- use enums inside real classes
- improve validation by replacing “magic strings” with enums

---

# Part 1 — Reading Notes

## 1. What problem are constants and enums solving?

Sometimes a variable should not accept just any value.

Examples:

- a course status might only be:
  - open
  - closed
  - cancelled

- a payment status might only be:
  - pending
  - paid
  - failed

- a ticket priority might only be:
  - low
  - medium
  - high

If we use plain strings everywhere, problems can happen:

```python id="51001"
status = "Open"
status = "open"
status = "OPEN"
status = "opne"
```

These are not all equally valid, but Python will allow them as plain strings.

That makes bugs easier.

---

## 2. What is a constant?

A constant is a value that should not change during the program.

Python does not enforce constants strictly, but by convention we write them in uppercase:

```python id="51002"
MAX_STUDENTS = 30
DEFAULT_CREDITS = 3
STATUS_OPEN = "open"
```

This tells other programmers:

- this value should be treated as fixed

---

## 3. What is an enum?

An enum is a special type used to define a fixed set of named values.

Example:

```python id="51003"
from enum import Enum

class Status(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"
```

Now the allowed values are much clearer and more controlled.

---

## 4. Why use enums instead of plain strings?

Enums help by:

- making allowed values explicit
- improving readability
- reducing spelling mistakes
- making validation easier
- improving program design

---

## 5. Constants vs enums

### Constants

Useful for:

- one fixed number
- one repeated fixed string
- configuration values

Example:

```python id="51004"
MAX_CAPACITY = 40
```

### Enums

Useful for:

- one variable that must be chosen from a known set of options

Example:

```python id="51005"
class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"
```

---

# Part 2 — Small Examples

## Example A — plain constants

```python id="51006"
STATUS_OPEN = "open"
STATUS_CLOSED = "closed"
STATUS_CANCELLED = "cancelled"

status = STATUS_OPEN
print(status)
```

This is better than typing random strings repeatedly, but it is still possible to assign:

```python id="51007"
status = "opne"
```

and Python will allow it.

---

## Example B — first enum

```python id="51008"
from enum import Enum

class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"
```

Use it:

```python id="51009"
status = CourseStatus.OPEN
print(status)
print(status.value)
```

---

## Example C — comparison

```python id="51010"
if status == CourseStatus.OPEN:
    print("Registration is allowed.")
```

This is clearer and safer than comparing loose strings.

---

## Example D — loop through enum values

```python id="51011"
from enum import Enum

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

for priority in Priority:
    print(priority, priority.value)
```

This is useful when you want to show all allowed choices.

---

# Part 3 — Important Concepts

## 1. Enum members are not plain strings

If you write:

```python id="51012"
status = CourseStatus.OPEN
```

then `status` is an enum member, not just `"open"`.

To get the underlying value:

```python id="51013"
print(status.value)
```

---

## 2. Compare with enum members, not random strings

Preferred:

```python id="51014"
if status == CourseStatus.OPEN:
    print("Open")
```

Less ideal:

```python id="51015"
if status.value == "open":
    print("Open")
```

When possible, compare with the enum member itself.

---

## 3. Enums help validation

If your class expects a status, you can require that it be a valid enum member.

That is much safer than accepting any string.

---

# Part 4 — Guided Build

## Build a `Course` class using an enum

Create these files:

- `status.py`
- `course.py`
- `main.py`

You may also put everything in one file if needed, but separate files are recommended.

---

# Step 1 — Create the enum

In `status.py`, create a `CourseStatus` enum.

```python id="51016"
from enum import Enum

class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"
```

---

# Step 2 — Create the `Course` class

In `course.py`, create a class called `Course`.

Each course should have:

- `title`
- `capacity`
- `status`

The `status` must use the enum, not a plain string.

# Step 3 — Validate the enum

Improve the constructor so that `status` must be a `CourseStatus` value.

Example idea:

```python id="51018"
from status import CourseStatus

class Course:
    def __init__(self, title, capacity, status):
        if not isinstance(status, CourseStatus):
            raise ValueError("status must be a CourseStatus value")

        self.title = title
        self.capacity = capacity
        self.status = status

    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value}")
```

This is a very important part of the session.

---

# Step 4 — Add methods that use the enum

Add:

- `close_registration()`
- `cancel_course()`
- `reopen_course()`

These methods should update the course status using the enum.

Example shape:

```python id="51019"
def close_registration(self):
    self.status = CourseStatus.CLOSED
```

---

# Step 5 — Test it in `main.py`

```python id="51020"
from course import Course
from status import CourseStatus

course1 = Course("Advanced Programming", 30, CourseStatus.OPEN)
course2 = Course("Web Interface Programming 2", 25, CourseStatus.CLOSED)

course1.display_info()
course2.display_info()

course1.close_registration()
course1.display_info()

course2.reopen_course()
course2.display_info()
```

---

# Part 5 — Add a property

Now improve the design.

Instead of exposing `status` as a normal public attribute, change it into a property with validation.

Use a private attribute such as:

```python id="51021"
self.__status
```

and create:

- `@property`
- `@status.setter`

So the class continues to enforce that only enum values are accepted.

---

## Example structure

```python id="51022"
@property
def status(self):
    return self.__status

@status.setter
def status(self, value):
    if not isinstance(value, CourseStatus):
        raise ValueError("status must be a CourseStatus value")
    self.__status = value
```

Then use:

```python id="51023"
self.status = status
```

inside the constructor.

This connects directly to the last sessions on:

- encapsulation
- properties
- invariants

---

# Part 6 — Required Independent Tasks

## Task 1 — Add a constant

Add at least one constant to your program, for example:

```python id="51024"
MAX_CAPACITY = 60
```

Use it to validate capacity in the `Course` class.

Example rule:

- capacity must be greater than 0
- capacity must not exceed `MAX_CAPACITY`

This helps you practice the difference between:

- constants
- enums

---

## Task 2 — Add a second enum

Create another enum called `DeliveryMode` with values such as:

- `ONLINE`
- `IN_PERSON`
- `HYBRID`

Add it to the `Course` class.

That means each course should now have:

- `status`
- `delivery_mode`

Both should be validated through enums.

---

## Task 3 — Add a second property

Add a property for `delivery_mode` so that only valid enum values are accepted.

---

## Task 4 — Improve `display_info()`

Your `display_info()` method should now display:

- title
- capacity
- status
- delivery mode

---

# Part 7 — Reflection Questions

Answer these briefly.

1. What is the difference between a constant and an enum?
2. Why are enums safer than random strings?
3. Why is `CourseStatus.OPEN` better than `"open"`?
4. Why did you use a property for `status`?
5. How do enums help validation in class design?

---

# Challenge Tasks

Complete at least **one**.

## Challenge 1 — Add `StudentLevel` enum

Create:

```python id="51025"
class StudentLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
```

Then build a small `Student` class that uses it.

---

## Challenge 2 — Restrict reopening rules

Modify `reopen_course()` so that:

- a cancelled course cannot be reopened directly
- only a closed course can reopen

This introduces a stronger business rule.

---

## Challenge 3 — Add a helper method

Add a method like:

```python id="51026"
is_open_for_registration()
```

that returns `True` only if the status is `CourseStatus.OPEN`.

---

## Challenge 4 — Add exception handling in `main.py`

Use `try/except` to show what happens when invalid values are passed.

Example:

```python id="51027"
try:
    bad_course = Course("Bad Course", 20, "open")
except ValueError as e:
    print("Error:", e)
```

---

# Things to Watch Out For

## 1. Do not compare enums to raw strings unless necessary

Prefer:

```python id="51028"
if course.status == CourseStatus.OPEN:
    print("Open")
```

instead of:

```python id="51029"
if course.status == "open":
    print("Open")
```

## 2. Remember that enum members are special objects

This is valid:

```python id="51030"
CourseStatus.OPEN
```

And this gives the underlying string:

```python id="51031"
CourseStatus.OPEN.value
```

## 3. Use properties for managed access

If your class must protect the allowed values, property setters are a good place for validation.

## 4. Do not confuse constants with enums

A constant is one fixed value.
An enum is a fixed set of choices.

## 5. Keep validation in the class

Do not depend only on outside code to pass correct values.
Your class should protect itself.
