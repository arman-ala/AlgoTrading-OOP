# Arman Ala
# 5 Aug, 2023
# Private Library Management Classes
genres = []
authors = []
books = []

class Genre:
    def __init__(self, genre_name):
        self.genre = None
        if genre_name is not None:
            self.genre = self.genre_name


class Author:
    def __init__(self, author_name=None, author_age=None, author_email=None):
        self.name = None
        self.age = None
        self.email = None
        if author_name is not None:
            self.name = author_name
        if author_age is not None:
            self.age = author_age
        if author_email is not None:
            self.email = author_email


    def __str__(self):
        return f"{self.name} - {self.age} - {self.email}"


class Book:
    def __init__(self, book_title, author_name, book_genre, book_pushed_date):
        self.title = None
        self.author = None
        self.genre = None
        self.published_date = None
        if book_title is not None:
            self.title = book_title
        if book_genre is not None:
            self.genre = book_genre
        if book_pushed_date is not None:
            self.published_date = book_pushed_date
        if author_name is not None:
            self.author = author_name


def add_genre(genre):
    if genre is not None:
        genres.append(genre)


def add_author(author_name):
    if author_name is not None:
        authors.append(author_name)


def add_book(book):
    if book is not None:
        books.append(book)