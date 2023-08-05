# Arman Ala
# 5 Aug, 2023
# Private Library Management Classes
genres = []
authors = []


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


def add_genre(genre):
    if genre is not None:
        genres.append(genre)


def add_author(self, author_name):
    if author_name is not None:
        authors.append(author_name)


class Book:
    pass
