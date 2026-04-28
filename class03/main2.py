class User:
    def __init__(self, username, email="N/A"): # default value for email
        self.username = username
        self.email = email


user1 = User("abc", "abc@canada.ca")
user2 = User("ddd") # we didn't put an email for this one. since we have a default value for it

print(user1.email)
print(user2.email)


# conditions inside of a method
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    
    # we need to control the behaviour here
    def sell_one(self):
        # let's impose some rules to the behaviour
        if self.stock > 0:
            self.stock = self.stock - 1
            print(f"sold 1!! now we have {self.stock} more left")
        else:
            print(f"{self.name} is out of stock")

product1 = Product("Mouse", 2)

product1.sell_one()
product1.sell_one()
product1.sell_one()
