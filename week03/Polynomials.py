from Monomials import Monomial


class Polynom:
    def __init__(self, poly):
        self.poly = poly
        self.poly_monomials = []
        for el in poly.split("+"):
            self.poly_monomials.append(Monomial(el))
        self.first_derivativ = self.get_first_derivativ()

    def get_first_derivativ(self):
        first_derivativ = []
        for mono in self.poly_monomials:
            if mono.is_constant:
                continue
            if mono.exponent != "":
                if mono.constant != "":
                        mono.constant = str(int(mono.constant) * int(mono.exponent[1:]))
                mono.exponent = "^" + str(int(mono.exponent[1:]) - 1)
                if mono.exponent == "^1":
                    mono.exponent = ""
            else:
                mono.variable = ""
            first_derivativ.append(mono)

        return "+".join([el.__str__() for el in self.poly_monomials])

    def __str__(self):
        return "The derivative of f(x) = {domain} is :\nf'(x) = {equasion}".format(
            domain=self.poly_monomials, equasion=self.first_derivativ)


p = Polynom("3x+4x^2")
q = Polynom("4x^6 + 5x^5 + 1")
print(q.__str__())
