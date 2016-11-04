class Fraction:

    def __init__(self, numer, denom):
        self.denom = denom
        self.numer = numer

    def __str__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return "{}/{}".format(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return "{}/{}".format(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return"{}/{}".format(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return"{}/{}".format(self.numer * other.denom, self.denom * other.numer)
