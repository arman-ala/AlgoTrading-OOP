# Arman Ala
# 5 Aug, 2023
# Private Library Management Classes
genres = []
authors = []
books = []

class Genre:
    def __init__(self, genre_name=None):
        self.genre = None
        if genre_name is not None:
            self.genre = genre_name
        else:
            self.genre = input("Please enter a Genre: ")
            # checking existance of genre in the list
            exists = False
            for genre in genres:
                if genre_name == genre.genre:
                    exists = True
            if exists == False:
                genres.append(self)
    
    
    def __str__(self):
        return self.genre


class Author:
    def __init__(self, author_name=None, author_age=None, author_email=None):
        self.name = None
        self.age = None
        self.email = None
        if author_name is not None and author_name != '':
            self.name = author_name
        else:
            self.name = input("Please enter author\'s name: ")
        if author_age is not None and author_age != '':
            self.age = author_age
        else:
            self.age = int(input("Please enter author\'s age: "))
        if author_email is not None and author_email != '':
            self.email = author_email
        else:
            self.email = input("Please enter author\'s email: ")
        # checking existance of author in the list
        exists = False
        for author in authors:
            if author_name == author.name:
                exists = True
        if exists == False:
            authors.append(self)
    
    
    def __str__(self):
        return f"{self.name} - {self.age} - {self.email}"


class Book:
    def __init__(self, book_title, book_pushed_date,\
        book_genre=None, author_name=None, author_age=None, author_email=None):
        self.title = None
        self.author = None
        self.genre = None
        self.published_date = None
        if book_title is not None or book_title != '':
            self.title = book_title
        if book_pushed_date is not None or book_pushed_date != '':
            self.published_date = book_pushed_date
        self.genre = Genre(book_genre)
        self.author = Author(author_name, author_age, author_email)
        # checking existance of author in the list
        exists = False
        for book in books:
            if book_title == book.title:
                exists = True
        if exists == False:
            books.append(self)


def add_genre(genre):
    if genre is not None:
        genres.append(genre)


def add_author(author_name):
    if author_name is not None:
        authors.append(author_name)


def add_book(book):
    if book is not None:
        books.append(book)
