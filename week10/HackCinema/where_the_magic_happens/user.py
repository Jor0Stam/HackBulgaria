from interface.METADATA import *


class User:

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return(USER_INFO).format(self.name)

    def __repr__(self):
        return(USER_INFO).format(self.name)


def main():
    pass


if __name__ == "__main__":
    main()
