from time import process_time


class Publisher:
    def __init__(self,name):
        self.name = name

class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        print(f"title:{self.title},author: {self.author},Publisher: {self.name}")

class Python(Book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.price=price
        self.pages=pages

    def display(self):
        super().display()
        print(f"price:{self.price},pages:{self.pages}")

book=Python("Wiley","introduction to python","john downey",650,320)
book.display()
