from json import dump


class Jsonable:

    def to_json(self, indent=4):
        return dump(self, indent=indent)

    @classmethod
    def from_json(json_string):
        pass


class Xmlable:

    def to_xml(self):
        pass

    @classmethod
    def from_xml(xml_string):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
