from HackCinema.interface import METADATA


class Movie:

    def __init__(self, id=None, title=None, raiting=0):
        self.id = id
        self.title = title
        self.raiting = raiting

    def __str__(self):
        return METADATA.MOVIE_INFO.format(self.title, self.raiting)

    def __repr__(self):
        return METADATA.MOVIE_INFO.format(self.title, self.raiting)


def main():
    mov = Movie("Avengers", 9.0)
    print(mov)


if __name__ == "__main":
    main()
