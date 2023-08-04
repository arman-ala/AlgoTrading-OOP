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
    pass


class Book:
    pass
