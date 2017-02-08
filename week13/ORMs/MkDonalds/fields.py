class Column:
    def check_type(self, data):
        if isinstance(data, self.data_type):
            return data
        raise TypeError(
            "Type of this column must be {}".format(self.data_type))


class PKColumn(Column):
    data_type = int

    def __init__(self, number=1):
        self.base_type = "INTEGER"

    def get_base_type(self):
        return self.base_type


class IntegerColumn(Column):
    data_type = int

    def __init__(self, number=1):
        self.base_type = "INTEGER"

    def get_base_type(self):
        return self.base_type


class TextColumn(Column):
    data_type = str

    def __init__(self, max_length=255):
        self.base_type = "TEXT ({})".format(max_length)

    def get_base_type(self):
        return self.base_type


def main():
    a = PKColumn()
    print(a.check_type("a"))


if __name__ == "__main__":
    main()
