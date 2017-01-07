from interface.METADATA import *
from subprocess import call
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
        print(command)
        if command == "exit":
            status = False


def main():
    pass


if __name__ == "__main__":
    main()
