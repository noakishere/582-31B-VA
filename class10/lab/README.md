# Lab: Encapsulation, Properties, and Invariants in Python Classes

## Objective

In this lab, you will design Python classes that protect their own data and prevent invalid object states.

You will use:

- private attributes
- properties
- setters
- validation
- methods
- invariants

The goal is to build classes that do not just store data, but also enforce rules so the object always remains valid.

## Core Concepts for This Lab

### 1. Encapsulation

Encapsulation means that a class should manage and protect its own internal data.

Instead of letting outside code change everything freely, the class should expose controlled ways to work with its data.

### 2. Private Attributes

In this lab, use private attributes with double underscores, for example:

```
self.__gpa
self.__credits
self.__capacity
```

These attributes should not be accessed directly from outside the class.

### 3. Properties

Use @property and setters to provide controlled access to private attributes.

This lets outside code use clean syntax like:

```
student.gpa = 3.8
```

while still allowing your class to validate the value behind the scenes.

### 4. Invariants

An invariant is a rule that must always remain true for an object.

Examples:

- GPA must stay between 0.0 and 4.0
- credits cannot be negative
- enrolled students cannot exceed course capacity
- capacity must always be greater than 0

Your class must protect these rules at all times.

## Lab Theme

### Safe Academic System

You will build classes from an academic domain and make sure they always remain valid.

You will create:

- StudentRecord
- CourseSection

Both classes must use:

- private attributes
- properties
- validation
- method-based updates
- invariant enforcement

## Files to Create

Create one or more of the following:

- `student_record.py`
- `course_section.py`
- `main.py`

## Part 1 — Build StudentRecord

Create a class called: `StudentRecord`

### Required public attribute

- `name`

### Required private attributes

- `__gpa`
- `__credits`

### Required invariants

Your class must ensure that:

- `name` cannot be empty
- GPA must always be between 0.0 and 4.0
- credits must always be greater than or equal to 0

### Required properties

Create properties for:

- gpa
- credits

Each must include:

- a getter
- a setter with validation

### Required methods

Add these methods:

- `add_credits(amount)`
- `update_gpa(value)`
- `display_info()`

#### Method expectations

`add_credits(amount)`

- adds credits if the amount is valid
- must not allow negative credit additions

`update_gpa(value)`

- updates GPA using the property
- must not allow invalid GPA values

`display_info()`

- prints the student information clearly.

## Part 2 — Build CourseSection

Create a class called: `CourseSection`

### Required public attribute

- `title`

### Required private attributes

- `__capacity`
- `__enrolled`

### Required invariants

Your class must ensure that:

- title cannot be empty
- capacity must always be greater than 0
- enrolled must always be greater than or equal to 0
- enrolled must never be greater than capacity

### Required properties

Create properties for:

- `capacity`
- `enrolled`

Each must include:

- a getter
- a setter with validation

### Required methods

Add these methods:

- `register_student()`
- `drop_student()`
- `display_info()`

#### Method expectations

`register_student()`

- increases enrolled count by 1
- must not allow enrollment beyond capacity

`drop_student()`

- decreases enrolled count by 1
- must not allow enrolled count to go below 0

`display_info()`

- prints the course information clearly

## Constructor Requirements

Both classes must validate their input during construction.

That means:

- an object should never be created in an invalid state
- the constructor must enforce the invariant from the beginning

A good design is to use your properties inside the constructor.

For example:

```
self.gpa = gpa
self.credits = credits
```

instead of assigning directly to the private fields without validation.

## Important Design Rule

Do not allow your methods to break the class rules.

For example:

- `register_student()` must not create a situation where enrolled > capacity
- `add_credits()` must not allow negative credit changes
- `update_gpa()` must not allow GPA outside the valid range

## Testing Requirements

In `main.py`, create test code that demonstrates:

### Valid cases

Your program must show examples of:

- valid object creation
- valid updates
- valid method calls

### Invalid cases

Your program must also show that invalid operations are rejected.

Examples:

- invalid GPA
- negative credits
- empty title
- course capacity of 0
- enrolling past capacity
- dropping students below 0

You may use `try/except` to display error messages clearly.

Example:

```
try:
student.update_gpa(5.0)
except ValueError as e:
print("Error:", e)
```

## Challenge Tasks

Complete at least one of the following.

## Challenge 1 — Add a computed property

In `StudentRecord`, add a read-only property:

`academic_status`

Rules:

- GPA >= 3.5 → "Honours"
- GPA >= 2.0 → "Good Standing"
- otherwise → "At Risk"

## Challenge 2 — Add a waitlist to CourseSection

Add a new private attribute:

`__waitlist`

Invariant:

- waitlist cannot be negative

Add methods:

- `add_to_waitlist()`
- `remove_from_waitlist()`

## Challenge 3 — Transfer a student between sections

Add a method or external function that transfers one student from one CourseSection to another.

Rules:

- source must have at least one enrolled student
- destination must have available capacity

## Challenge 4 — Use exceptions consistently

Make your validation use ValueError with clear messages everywhere instead of only printing warnings
