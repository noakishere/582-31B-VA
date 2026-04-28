# method-writing practice

class Book:
    def __init__(self, title, author, available = True):
        self.title = title # string
        self.author = author # string
        self.available = available # boolean --> True or False
        print(f"{self.title} added successfully")

    # lend a book (borrow to someone)
    def borrow(self):
        if(self.available == False):
            print(f"{self.title} is already borrowed. Sorry!")
        else:
            self.available = False
            print(f"{self.title} has been borrowed.")

    # return the book (get it back)
    def return_book(self):
        if(self.available == False):
            self.available = True
            print(f"{self.title} has been returned, thank you!")
        else:
            print(f"I don't think that's my copy! I already have {self.title}")

    # show the status
    def show_status(self):
        print(f"{self.title} availability: {self.available}")


book1 = Book("A Song of Ice and Fire", "George R.R. Martin")

book1.borrow()
book1.borrow()
book1.return_book()
book1.borrow()

book2 = Book("Clean Code", "Robert C. Martin", False)
book2.borrow()

book1.return_book()
book1.show_status()
book2.show_status()