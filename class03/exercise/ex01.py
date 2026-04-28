# create a class of Fruit
class Fruit:
    # give it 3 attributes (1 should be price)
    def __init__(self, name, price, origin):
        self.name = name
        self.price = price
        self.origin = origin

    # define 3 methods that access the attributes and return them
    def get_origin(self):
        return self.origin

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
    
    # define a method that changes the price to a new price (taken as an parameter)
        # and returns the new price (USUALLY, WE DONT RETURN FOR SETTERS)
    def set_price(self, new_price):
        self.price = new_price
        print(f"New price is set to {new_price}!")
    
fruit1 = Fruit("Durian", 10, "Vietnam")
fruit2 = Fruit("Apple", 20, "Canada")
fruit3 = Fruit("Orange", 5, "California")

fruit2.set_price(15)

fruits = [fruit1, fruit2, fruit3]

for fruit in fruits:
    print(f"{fruit.get_name()} is ${fruit.get_price()} and it's from {fruit.get_origin()}")

