#Inheritance

# what happens when several classes are related and should share common behaviour
# without duplicating code??

# but first, let's do a quick recap:

# Encapsulation:

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    
# Encapsulation says: object state shold be protected intentionally.

# Properties:

# let us keep clean attribute syntax
# validate and/or controll access to our attributes

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

    @property
    def gpa(self):
        return self.__gpa ## define private attribute
    
    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0: # This is an invariant!
            self.__gpa = value
        else:
            raise ValueError("Invalid GPA")

# properties make controlled access feel natural!


# Invariants:

# what is an invariant? it's a rule that must always remain true
# good classes prevent invalid states


# Constans and Enums


from enum import Enum

# once value is set, you cannot change it in runtime in Pythonn
class CourseStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"

status = CourseStatus.OPEN

print(status.value)

# enums reduce invalid values and improve readability.

# for example: CourseStatus class becomes a container for a series of constants.


# all of the concepts above help us design one class properly. 


# why inheritance exists?

# Inheritance lets one class reuse and extend another class.

# A parent class : A more general class

# A child class : a more specific class that inherits from the parent

# Suppose you are building different kinds of users in a system.

# You might have: User - StudentUser - AdminUser
# They may all share: 
#   username
#   email
#   password
#   name
#   address
#   phone_number

# they may differ in:
#   students have a program
#   admins have departments

# without inheritance, we have to repeat the code across several classes.
# with inheritance, the child can reuse common parent behaviour.

# Inheritance = shared structure + specialization

class User:
    def __init__(self, username):
        print("hello from parent constructor")
        self.username = username

    def introduce(self):
        print(f"Hello, my name is {self.username}")
    

class StudentUser(User): #extending the User class
    def __init__(self, username, program):
        super().__init__(username) # super means go to the parent class
                                   # and in here we refer to the parent class' constructor
        print("hello from child constructor")
        self.program = program

class AdminUser(User):
    def __init__(self, username, dpt):
        super().__init__(username)

        self.dpt = dpt

student1 = StudentUser("Jane", "Web Dev")
student1.introduce() # StudentUser uses the function from the parent class
print(student1.program)

admin1 = AdminUser("John", "Accounting")
admin1.introduce()
# print(admin1.program)

# StudentUser(User): this basically means StudentUser inherits from User
# StudentUser gets access to inherited methods like introduce()
# super().__init__(name) calls parent
    # super is very important. because without the parent setup might not happen!
    # double important when the parent constructor initializes important shared data.


# The difference between abstract classes and inheritance:
#   abstract classes define strict rules on what functions need to be implemented by the class.
#   inheritance allows one Parent class to pass down functions and attributes to a child class.


# ===============
print("=============")

# Method overriding

# a child class can replace or customize inherited behaviour --> this is called overriding.

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Employee(Person):
    def __init__(self, name, dpt):
        super().__init__(name)
        
        self.dpt = dpt
    
    # we're overriding the parent function
    def introduce(self):
        print(f"Hello, my name is {self.name} and I work at the {self.dpt}")

person = Person("John")
employee = Employee("Jane", "Software Development")

person.introduce()
employee.introduce()

# both classes have an introduce() method, but the child version replaces the parent version
# for employee objects.

class Admin(Person):
    def __init__(self, name, dpt):
        super().__init__(name)
        self.dpt = dpt

    # we override and use the parent method
    def introduce(self):
        super().introduce() # first execute parent method
        print(f"I oversee the {self.dpt} department") # then add the overriden stuff

admin = Admin("Alice", "Software Development")
admin.introduce()

# super() means go to the parent class!

# let's move on to
# Polymorphism

# Polymorphism means different objects can respond to the same method call in their own way

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, my name is {self.name} and I teach {self.subject}")


print("========")
people = [
    Person("Nadia"),
    Employee("Ahmed", "Accounting"),
    Admin("Janice", "HR"),
    Teacher("Mr. A", "Mathematics")
]

for person in people:
    person.introduce()

# the idea of polymorphism is that the same method works on all objects, but each object responds differently.

# another example:
print()
print("===========")

class Notification:
    def send(self, message):
        print(f"Generic notification: {message}")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

class FaxNotification(Notification):
    def send(self, message):
        super().send(message)
        print(f"via fax")

notifications = [EmailNotification(), SMSNotification(), FaxNotification(), Notification()]

for notification in notifications:
    notification.send("Hello!") # polymorphism!


# Polymorphism linguistically means : many forms (from Greek)
#   refers (soft. dev) to the ability of different data types, objects, or functions to share the same interface.
#   it allows a single symbol or method to behave differently, depending on the context!