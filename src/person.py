
class Person:
    def __init__(self, name, gender, address, age):
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def as_dict(self):
        return self.__dict__
