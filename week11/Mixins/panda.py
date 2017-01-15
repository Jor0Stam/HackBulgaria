from json import dumps, loads
import lxml.etree as ET


class JsonableMixin:

    def to_json(self, indent=4):
        data = {'dict': self.__dict__, 'Classname': self.__class__.__name__}
        return dumps(data, indent=indent)

    @classmethod
    def from_json(cls, json_string):
        data = loads(json_string)
        classname = data.get('Classname')

        if classname != cls.__name__:
            raise ValueError('{} is not {}!'.format(cls.__name__, classname))
        return cls(**data["dict"])


class XmlableMixin:

    def to_xml(self):
        root_el = ET.Element(self.__class__.__name__)
        for k, v in self.__dict__.items():
            key = ET.SubElement(root_el, k, {"Type": type(v).__name__})
            key.text = str(v)
        return ET.tostring(root_el).decode("utf-8")


    @classmethod
    def from_xml(cls, xml_string):
        types = {'int': int, 'str': str, 'list': list, 'dict': dict,
                 'tuple': tuple, 'float': float}
        root = ET.fromstring(xml_string)
        if root.tag != cls.__name__:
            raise ValueError('{} is not {}!'.format(cls.__name__, root.tag))
        data = {}
        for child in root:
            data[child.tag] = types[child.attrib['Type']](child.text)

        return cls(**data)


class Panda(JsonableMixin, XmlableMixin):

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}".format(self.name)

    def __eq__(self, other):
        return self.args == other.args and self.kwargs == other.kwargs

    def __hash__(self):
        return hash(self.kwargs)


def main():
    # p1 = Panda(name="Pandarian", age=20)
    # json_string = p1.to_json()
    # print(Panda().from_json(json_string))
    p2 = Panda(name="Older Pandarian", age=20)
    xml_string = p2.to_xml()
    print(xml_string)
    print(Panda().from_xml(xml_string))
    print(type(Panda().from_xml(xml_string).age))


if __name__ == "__main__":
    main()
