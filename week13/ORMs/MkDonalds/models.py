import sqlite3
from settings import db_name
from base import FieldsMeta


def format_fields(fields):
    res = ""
    for key, value in fields.items():
        res += " " + key + " " + value.get_base_type() + ","
    print("THIS ->", res)
    return res[:-1]


def create_table(tablename, fields, cur):
    print(tablename)
    cur.execute("CREATE TABLE IF NOT EXISTS " +
                tablename + "(" + format_fields(fields) + " )")


# create enough question marks
def get_q_m(values):
    if len(values) == 0:
        return ""
    if len(values) == 1:
        return "?"
    return "?, " * (len(values) - 1) + "?"


def create_record(tablename, kwargs, cur):
    key_names = tuple(key for key, value in kwargs.items())
    values = tuple(value for key, value in kwargs.items())
    q_m = "(" + get_q_m(values) + ")"
    cur.execute(
        "INSERT INTO " + tablename + " " + str(key_names) + " VALUES " + q_m,
        values)


def key_value(key, value):
    return str(key) + "=" + str(value)


def format_filter(kwargs):
    if not kwargs:
        return ""
    return " WHERE " + " AND ".join([key_value(key, value)
                           for key, value in kwargs.items()])


def filter_it(tablename, kwargs, cur):
    wheres = format_filter(kwargs)
    print("SELECT * FROM " + tablename + wheres)
    cur.execute("SELECT * FROM " + tablename + wheres)


class BaseModel(metaclass=FieldsMeta):
    __tablename__ = None

    @classmethod
    def create_all_tables(cls):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        for table in cls._registry:
            create_table(table.__tablename__, table._fields, cur)
        conn.commit()

    @classmethod
    def create_obj(cls, **kwargs):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        create_record(cls.__tablename__, kwargs, cur)
        conn.commit()

    @classmethod
    def filter(cls, **kwargs):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        filter_it(cls.__tablename__, kwargs, cur)


def main():
    pass


if __name__ == "__main__":
    main()
