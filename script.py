from src.book import Book
from src.person import Person
import json

from files import CSV_FILE_PATH
from files import JSON_FILE_PATH
from files import JSON_RESULT_PATH
from csv import DictReader

books = []

with open(CSV_FILE_PATH, 'r', newline='') as csvfile:
    booksJson = DictReader(csvfile)
    for row in booksJson:
        asData = json.loads(json.dumps(row))
        book = Book()
        book.set_title(asData['Title'])
        book.set_author(asData['Author'])
        book.set_pages(asData['Pages'])
        book.set_genre(asData['Genre'])
        books.append(json.dumps(book.__dict__))

persons = []

file = open(JSON_FILE_PATH, "r")
users = json.loads(file.read())
for user in users:
    person = Person()
    person.set_name(user["name"])
    person.set_gender(user["gender"])
    person.set_address(user["address"])
    person.set_age(user["age"])
    persons.append(person)


while len(books) > 0:
    for person in persons:
        if len(books) > 0:
            person.add_book(books.pop())

personsJson = []

for person in persons:
    personJson = json.dumps(person.__dict__)
    personsJson.append(personJson)

print(personsJson)


with open(JSON_RESULT_PATH, "w", ) as f:
    s = json.dumps(personsJson, indent=4)
    f.write(s)
