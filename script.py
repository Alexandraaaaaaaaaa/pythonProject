from src.book import Book
from src.person import Person
import json

from files import CSV_FILE_PATH
from files import JSON_FILE_PATH
from files import JSON_RESULT_PATH
from csv import DictReader

books = []

with open(CSV_FILE_PATH, 'r', newline='') as csvfile:
    books_json = DictReader(csvfile)
    for row in books_json:
        asData = json.loads(json.dumps(row))
        book = Book(asData['Title'], asData['Author'], asData['Pages'], asData['Genre'])
        books.append(book)

persons = {}

file = open(JSON_FILE_PATH, "r")
users = json.loads(file.read())
for user in users:
    person = Person(user["name"], user["gender"], user["address"], user["age"])
    persons.update({user['_id']: person.as_dict()})

while len(books) > 0:
    for key in persons:
        if len(books) > 0:
            current_book = books.pop()
            persons[key]['books'].append(current_book.as_dict())

with open(JSON_RESULT_PATH, "w", ) as f:
    s = json.dumps(persons, indent=4)
    f.write(s)
