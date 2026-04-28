# mistake 1 -- forgetting self
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(): # WE NEED TO PASS SELF AS A PARAMETER , ALWAYS!!!!!!
        self.stock -= 1


# mistake 2 -- forgeting self. for attributes!
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(self):
        stock -= 1 # if you don't put self. before attribute name , it won't recognize it! IMPORTANT!!!

product = Product("test", 1)
print(product.stock)
product.sell_one()
print(product.stock)

# Mistake 3
Product.sell_one() # THIS IS NOT CORRECT, DONT CALL CLASS NAME (Product vs product--instance)
# product.sell_one()

# Mistake 4
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell_one(self):
        # this doesn't change anything! MISTAKE!
        self.stock - 1

        # these are statements, changing state CORRECTLY
        self.stock = self.stock - 1
        self.stock -= 1

# Mistake 5
# dont mix printing and returning with eachoter!
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def get_name(self):
        # these two are NOT EQUAL
        print(self.name) # used for quick demonstration
        return self.name # when the result/value needs to be stored/used elsewhere