from hospital_queries import *
import sqlite3
from METADATA import *
from prettytable import PrettyTable


def show_patients():
    manager = sqlite3.connect(DB_NAME)
    manager.row_factory = sqlite3.Row
    c = manager.cursor()

    c.execute(list_all_patients)
    patients = c.fetchall()
    c.close()
    return(make_it_pretty(patients))


def make_it_pretty(to_p):
    result = PrettyTable(to_p)
    for row in to_p:
        print(row)
        # result.add_row(row)


def main():
    print(show_patients())


if __name__ == "__main__":
    main()
