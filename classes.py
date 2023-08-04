# Arman Ala
# 5 Aug, 2023
# Private Library Management Classes

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
        if author_email is not None:
            self.email = author_email



class Book:
    pass
