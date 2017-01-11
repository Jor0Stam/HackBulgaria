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


def are_you_god():
    clear(ARE_YOU_GOD)
    usr = input("User: ")
    password = getpass("GodPass: ")
    status = False
    if usr == "j" and password == "j1":
        status = True
    while status:
        print(1)
        clear(ADD_MOVIE_MENU)
        command = input(">")
        if command in ["return"]:
            initiate_HackCinema()
        elif command in ["exit"]:
            raise SystemExit(0)
        elif command in ["add", "new"]:
            name = input("Movie title: ")
            rate = input("Movie rating: ")
            add_movie_to_db(name, rate)


def are_you_god2():
    clear(ARE_YOU_GOD)
    usr = input("User: ")
    password = getpass("GodPass: ")
    status = False
    if usr == "j" and password == "j1":
        status = True
    while status:
        print(1)
        clear(ADD_PROJECTION_MENU)
        command = input(">")
        if command in ["return"]:
            initiate_HackCinema()
        elif command in ["exit"]:
            raise SystemExit(0)
        elif command in ["add", "new"]:
            movie_id = input("Movie ID: ")
            p_type = input("Type: ")
            p_date = input("Date: ")
            p_time = input("Time: ")
            add_projection_to_db(movie_id, p_type, p_date, p_time)


def initiate_HackCinema(mssg=False):
    cast_text_to_green()
    status = True
    if mssg:
        clear(WELCOME_SCREEN + '\n' + mssg)
    else:
        clear(WELCOME_SCREEN)
    while status:
        command = input(">")
        if command in ["log in"]:
            if log_to_sys():
                status = False
        elif command in ["register"]:
            register()
        elif command in ["add", "add movie"]:
            are_you_god()
        elif command in ["add proj"]:
            are_you_god2()
        elif command in ["exit"]:
            raise SystemExit(0)
    main_menu()


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
    initiate_HackCinema(USER_CREATED)


def main():
    cast_text_to_green()
    print("Hello, greenys!")


if __name__ == "__main__":
    main()
