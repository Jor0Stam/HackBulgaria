from MkDonalds.fields import Column
from collections import OrderedDict


class RegistryMeta(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)

        if not hasattr(clsobj, '__tablename__'):
            raise AttributeError("Models must have __tablename__ attr!")

        if not hasattr(clsobj, "_registry"):
            clsobj._registry = set()

        if clsobj.__tablename__:
            clsobj._registry.add(clsobj)

        return clsobj


class FieldsMeta(RegistryMeta):

    def __new__(cls, name, bases, clsdict):

        _fields = [(attr_name, clsdict[attr_name])
                   for attr_name, attr_class in clsdict.items()
                   if isinstance(attr_class, Column)]

        clsdict["_fields"] = OrderedDict(_fields)

        return super().__new__(cls, name, bases, clsdict)


def main():
    pass


if __name__ == "__main__":
    main()
