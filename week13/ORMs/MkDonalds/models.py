import sqlite3
from settings import db_name
from base import FieldsMeta


def create_table(tablename, cur):
    print(tablename)
    cur.execute("CREATE TABLE test(testcolumn text)")


class BaseModel(metaclass=FieldsMeta):
    __tablename__ = None

    @classmethod
    def create_all_tables(cls):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        for table in cls._registry:
            create_table(table.__tablename__, cur)
        # cur.commit()
        # cur.flush()


def main():
    pass


if __name__ == "__main__":
    main()
