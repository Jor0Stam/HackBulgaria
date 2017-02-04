class basetracking(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)

        if not hasattr(cls, 'registry'):
            cls.registry = set()

        cls.registry.add(clsobj)

        return clsobj


class Base(metaclass=basetracking):
    pass


class A(Base):
    pass


class B(Base):
    pass
    # def __init__(self):
    #     pass


class C(A):  # , B):
    pass
    # def __init__(self, a, b, *args, **kwargs):
    #     pass


print(Base.registry)


class Manqk(object):
    a = 5

    def __init__(self, neshto=2):
        self.neshto = neshto


m = Manqk(neshto=3)
