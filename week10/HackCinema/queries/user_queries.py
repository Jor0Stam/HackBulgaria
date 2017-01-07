from queries.queries import *
import sqlite3
from settings import sql_create_settings as sett
# from interface.decorators import *


def initiate_database():
    hackCinema = sqlite3.connect(sett.DB_NAME)
    hackCinema.row_factory = sqlite3.Row
    return hackCinema


def check_user_exist(username, password):
    hackCinema = initiate_database()
    c = hackCinema.cursor()

    c.execute(get_user, (username, password,))
    status = c.fetchall()
    if status:
        return True
    return False


def takken_name(username):
    hackCinema = initiate_database()
    c = hackCinema.cursor()

    c.execute(check_name, (username,))
    status = c.fetchall()
    if status:
        return True
    return False


# @encrypt()
def go_for_password(password):
    return password


def add_user(username, password):
    if takken_name(username):
        return False
    hackCinema = initiate_database()
    c = hackCinema.cursor()
    return True

    c.execute(create_usr, (username, go_for_password(password)))


def main():
    check_user_exist("a", "b")


if __name__ == "__main__":
    main()
