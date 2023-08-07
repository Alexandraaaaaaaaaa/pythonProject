class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = int(pages)
        self.genre = genre

    def as_dict(self):
        return self.__dict__

