# Arman Ala
# 5 Aug, 2023
# Private Library Management Classes
import re


class Genre:
    def __init__(self, *args):
        self.genres = []
        if len(args) > 0:
            self.genres.extend(args)

    def add_genre(self, genre):
        if genre:
            self.genres.append(genre)
            return True
        else:
            return False


class Author:
    def __init__(self, author_name=None, author_age=None, author_email=None):
        self.name = None
        self.age = None
        self.email = None
        if author_name is not None:
            self.name = author_name
        if author_age is not None:
            self.age = author_age
        if author_email is not None and self.check_email:
            self.email = author_email


    def check_email(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
        if re.match(pattern, self.email):
            return True
        else:
            return False


class Book:
    pass
