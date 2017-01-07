import sqlite3
from settings import sql_create_settings as sett
from queries.queries import *


def create_tables():
    hackCinema = sqlite3.connect(sett.DB_NAME)
    hackCinema.row_factory = sqlite3.Row
    c = hackCinema.cursor()

    c.execute(drop_db_m)
    hackCinema.commit()

    c.execute(drop_db_p)
    hackCinema.commit()

    c.execute(drop_db_u)
    hackCinema.commit()

    c.execute(drop_db_r)
    hackCinema.commit()

    hackCinema.execute(create_movies_table)
    hackCinema.execute(create_reservations_table)
    hackCinema.execute(create_users_table)
    hackCinema.execute(create_projections_table)
    hackCinema.commit()


def main():
    create_tables()


if __name__ == "__main__":
    main()
