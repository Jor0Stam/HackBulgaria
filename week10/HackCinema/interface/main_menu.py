from interface.METADATA import *
from subprocess import call
from queries.user_queries import *
# from interface.log_menu import clear


def clear(mssg=None):
    call(["clear"])
    if mssg:
        print(mssg)


def main_menu():
    clear(HELP)
    status = true
    while status:
        command = input(">")
        if command in ["exit"]:
            status = False
        elif command in ["show movies"]:
            print(show_movies())
        elif command in ["show movies projections {} {}"]:
            print(show_movies())
        elif command in ["reserve"]:
            print(show_movies())


def main():
    pass


if __name__ == "__main__":
    main()
