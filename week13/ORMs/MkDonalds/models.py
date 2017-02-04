import sqlite3
from settings import db_name
from MkDonalds.base import FieldsMeta


def create_table(tablename, datab):
    c = datab.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS ()")


class BaseModel(metaclass=FieldsMeta):
    __tablename__ = None

    new_db = sqlite3.connect(db_name)
    new_db.row_factory = sqlite3.Row
    cur = new_db.Cursor()

    @classmethod
    def create_all_tables(cls):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
