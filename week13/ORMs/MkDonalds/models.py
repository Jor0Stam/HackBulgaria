import sqlite3
from settings import db_name
from base import FieldsMeta


def format_fields(fields):
    res = ""
    for key, value in fields.items():
        res += " " + key + " " + value.get_base_type()
    print("THIS ->", res)
    return res  #" data INTEGER "


def create_table(tablename, fields, cur):
    print(tablename)
    cur.execute("CREATE TABLE IF NOT EXISTS " +
                tablename + "(" + format_fields(fields) + " )")


class BaseModel(metaclass=FieldsMeta):
    __tablename__ = None

    @classmethod
    def create_all_tables(cls):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        for table in cls._registry:
            create_table(table.__tablename__, table._fields, cur)
        # cur.commit()
        # cur.flush()


def main():
    pass


if __name__ == "__main__":
    main()
