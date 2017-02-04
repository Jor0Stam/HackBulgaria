class Column:
    pass


class PKColumn(Column):
    def __init__(self, autoincrement):
        self.autoincrement = autoincrement

    def __str__(self):
        return "ID"

    def __repr__(self):
        return "ID"


class IntegerColumn(Column):

    def __init__(self, number=100):
        self.number = number

    def __str__(self):
        return "INTEGER"

    def __repr__(self):
        return "INTEGER"


class TextColumn(Column):

    def __init__(self, max_length=100):
        self.max_length = max_length

    def __str__(self):
        return "TEXT"

    def __repr__(self):
        return "TEXT"


def check_type(value, my_type):
        try:
            return my_type(value)
        except ValueError:
            print("This must be {t} -> {v}".format(t=my_type.__name__,
                                                   v=value))


def main():
    a = PKColumn("asd")


if __name__ == "__main__":
    main()
