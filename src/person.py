from src.book import Book


class Person:
    def __init__(self):
        self.name = None
        self.gender = None
        self.address = None
        self.age = None
        self.books = []

    def set_name(self, name: str):
        self.name = name

    def set_gender(self, gender: str):
        self.gender = gender

    def set_address(self, address: str):
        self.address = address

    def set_age(self, age):
        self.age = age

    def add_book(self, book):
        self.books.append(book)
