from queries.queries import *
import sqlite3
from settings import sql_create_settings as sett
from interface.decorators import *
from passlib.hash import pbkdf2_sha256
from where_the_magic_happens.projection import *


projections = {}


def initiate_db():
    hackCinema = sqlite3.connect(sett.DB_NAME)
    hackCinema.row_factory = sqlite3.Row
    return hackCinema


def check_user_exist(username, password):
    hackCinema = initiate_db()
    c = hackCinema.cursor()
    c.execute(get_user, (username,))
    status = c.fetchone()
    if status["NAME"] == username and pbkdf2_sha256.verify(password,
                                                           status["PASSWORD"]):
        return True
    return False


@encrypt()
def go_for_password(password):
    return password


def add_user(username, password):

    if takken_name(username):
        return False
    hackCinema = initiate_db()
    c = hackCinema.cursor()
    c.execute(create_user, (username, go_for_password(password)))
    hackCinema.commit()
    hackCinema.close()
    return True


def show_movies():
    hackCinema = initiate_db()
    c = hackCinema.cursor()
    result = c.execute(get_movies_by_rate)
    hackCinema.commit()
    return result


def add_movie_to_db(name, rate):
    hackCinema = initiate_db()
    c = hackCinema.cursor()
    c.execute(add_movie, (name, rate,))
    hackCinema.commit()


def add_projection_to_db(m_id, m_type, m_date, m_time):
    hackCinema = initiate_db()
    c = hackCinema.cursor()
    c.execute(add_projection, (m_id, m_type, m_date, m_time,))
    hackCinema.commit()
    global projections
    if m_id in projections.keys():
        projections[m_id].extend(Projection(m_id, m_type, m_date, m_time))
    else:
        projections[m_id] = [Projection(m_id, m_type, m_date, m_time)]


def show_movie_projections(m_id, m_date):
    hackCinema = initiate_db()
    c = hackCinema.cursor()
    if m_date:
        c.execute(show_projections_d, (m_id, m_date,))
    else:
        c.execute(show_projections, (m_id,))
    return c.fetchall()


def main():
    a = go_for_password("a")
    print(a == go_for_password("a"))


if __name__ == "__main__":
    main()
