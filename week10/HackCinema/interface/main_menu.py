from interface.METADATA import *
from subprocess import call
from queries.user_queries import *


def clear(mssg=None):
    call(["clear"])
    if mssg:
        print(mssg)


def show_all_movies():
    clear(MOVIES)
    result = ""
    for row in show_movies():
        result += "\n" + (MOVIE_FORMAT.format(row[ID],
                                              row[NAME],
                                              row[RAITING]))
    if not result:
        result = "None"
    clear(MOVIES + result)


def show_m_projections():
    show_all_movies()
    m_id = input("Choose a movie (id)!: ")
    m_date = input("Choose a date!: ")
    result = ""
    for row in show_movie_projections(m_id, m_date):
        result += "\n" + (PROJECTION_FORMAT.format(m=show_movies[m_id]["NAME"],
                                                   ty=row["TYPE"],
                                                   d=row["M_DATE"],
                                                   ti=row["M_TIME"]))
    if not result:
        result = "None"
    clear(PROJECTIONS + result)


def seats_takken(m_id, seats):
    if len(movies[m_id].get_seats()) >= len(seats):
        return False
    return True


def take_seats(m_id, seats):
    pass


def reserve():
    m_id = input(CHOOSE_ID)
    if m_id == "give up":
            main_menu()
    seats = input(CHOOSE_SEATS)
    if seats == "give up":
            main_menu()
    while seats_takken(m_id, seats):
        print(NO_SEATS)
        seats = input(CHOOSE_SEATS)
        if seats == "give up":
            main_menu()
    take_seats(m_id, seats)


def main_menu():
    clear(HELP)
    while True:
        command = input(">")
        if command in ["exit"]:
            raise SystemExit(0)
        elif command in ["help"]:
            clear(HELP_MENU)
        elif command in ["show movies"]:
            show_all_movies()
        elif command in ["show projections"]:
            show_m_projections()
        elif command in ["reserve"]:
            clear("COMING SOON !!!")
            show_movies()
            reserve()


def main():
    pass


if __name__ == "__main__":
    main()
