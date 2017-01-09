from queries.queries import *
import sqlite3
from settings import sql_create_settings as sett
from interface.decorators import *
from time import sleep


def initiate_database():
    hackCinema = sqlite3.connect(sett.DB_NAME)
    hackCinema.row_factory = sqlite3.Row
    return hackCinema


def check_user_exist(username, password):
    # hackCinema = initiate_database()
    hackCinema = sqlite3.connect(sett.DB_NAME)
    hackCinema.row_factory = sqlite3.Row
    c = hackCinema.cursor()

    c.execute(get_user, (username,))
    # status = c.fetchone()
    print(c.execute(get_user, (username,)).fetchone())
    sleep(5)
    c.close()
    # if status and pbkdf2_sha256.verify(password, status[0][0]):
    #     return True
    # return False


def takken_name(username):
    hackCinema = initiate_database()
    c = hackCinema.cursor()

    c.execute(check_name, (username,))
    status = c.fetchall()
    c.close()
    if status:
        return True
    return False


@encrypt()
def go_for_password(password):
    return password


def add_user(username, password):
    if takken_name(username):
        return False
    hackCinema = initiate_database()
    c = hackCinema.cursor()

    c.execute(create_user, (0, username, go_for_password(password)))
    hackCinema.commit()
    hackCinema.close()
    return True


def show_movies():
    hackCinema = initiate_database()
    c = hackCinema.cursor()
    result = c.execute(get_movies_by_rate)
    c.close()
    return result


def main():
    a = go_for_password("a")
    print(a == go_for_password("a"))


if __name__ == "__main__":
    main()
