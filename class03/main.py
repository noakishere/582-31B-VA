class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # the type of this function/method is VOID
    def desc(self): # all methods in the class should take in at least self as a parameter
        print(f"{self.name} is ${self.price}")

    # this is a return function
    def get_name(self):
        return self.name
    
    def discounted_price(self):
        new_price = self.price - 5
        return new_price

product1 = Product("Keyboard", 59.99)

# print(product1.name, product1.price)
product1.desc()
str = product1.get_name()
print(f"I want to buy a new {str}")

product1_new_price = product1.discounted_price()
print(f"You're lucky, the new price is ${product1_new_price}")

# if we want the product to describe itself, change price, check availability, etc.
# we would need METHODS


# let's define what a method is: 
#   a method is a function defined inside a class that represents behaviour
#   belonging to an object.


# attributes = what the object HAS
# methods = what the object DOES

# what's the difference between these two?
print(product1.name)  # taking the raw data! from our instance , or whatever's available in the class
print(product1.get_name()) # we're accessing a defined behaviour by the object.



# let's get more into what self refers to

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def show_role(self):
        print(f"{self.username} has role: {self.role}")

user1 = User("nina", "admin")
user2 = User("leo", "student")

user1.show_role()
user2.show_role()

# self is the instance the method is working on.

