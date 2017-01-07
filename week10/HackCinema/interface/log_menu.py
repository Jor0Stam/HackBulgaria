from colorama import Fore
from subprocess import call
from interface.METADATA import *
from getpass import getpass
from queries.user_queries import *
from interface.main_menu import *
from re import search


def clear(mssg=None):
    call(["clear"])
    if mssg:
        print(mssg)


def cast_text_to_green():
    print(Fore.GREEN)


def initiate_HackCinema():
    cast_text_to_green()
    status = True
    clear(WELCOME_SCREEN)
    while status:
        command = input(">")
        if command == "log in":
            if log_to_sys():
                print("ENTERED")
                status = False
        elif command == "register":
            register()
        elif command == "exit":
            raise SystemExit(0)


def log_to_sys():
    clear()
    username = input("Username: ")
    password = getpass("Password: ")

    while not check_user_exist(username, password):
        clear(FAIL_LOG_IN)
        username = input("Username: ")
        password = getpass("Password: ")
    return True


def incorrect_password(password):
    return not(search(r"\d", password) and search(r"[A-Z]", password) and
               search(r"[a-z]", password) and len(password) > 6)


def register(mssg=None):
    clear(mssg)
    username = input(USR_INP)
    password = "Not Repeat Password"
    repeat_password = "Not Password!"
    while password != repeat_password or incorrect_password(password):
        password = getpass(PASS_INP)
        repeat_password = getpass(REPEAT_PASS)
        if password != repeat_password:
            register(PASS_ERR)
        if incorrect_password(password):
            register(PASS_INCORECT)
    if not add_user(username, password):
        register(USER_EXIST)
    else:
        print(USER_CREATED)
    initiate_HackCinema()


def main():
    cast_text_to_green()
    print("Hello, greenys!")


if __name__ == "__main__":
    main()
