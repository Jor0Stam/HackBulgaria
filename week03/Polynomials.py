from Monomials import Monomial


class Polynom:
    def __init__(self, poly):
        self.poly = poly
        self.poly_monomials = self.to_monomials(poly)
        self.first_derivativ = self.get_first_derivativ()

    def __str__(self):
        return "The derivative of f(x) = {domain} is :\nf'(x) = {equasion}".format(
            domain=self.poly, equasion=self.first_derivativ)

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
                mono.constant = 1 * mono.get_constant()
            first_derivativ.append(mono)

        # return "+".join([el.__str__() for el in first_derivativ])
        result = "+".join([el.__str__() for el in self.simplify_by_exponents(first_derivativ)])
        if result == "":
            return 0
        return result

    def simplify_by_exponents(self, equasion):
        simple_eq = {}
        for ind in range(self.greatest_exponent(equasion) + 1):
            simple_eq[ind] = self.get_by_exponent(equasion, ind)

        return list(simple_eq.values())

    def get_by_exponent(self, equasion, exp):
        if exp == 0:
            result = Monomial("0")
            for el in equasion:
                if el.variable == "":
                    result.add_to_const(str(int(el.get_constant())))
            if result == 0:
                return ""
            return result
        elif exp == 1:
            result = Monomial("x")
        else:
            result = Monomial("x{exp}".format(exp="^" + str(exp)))
        for el in equasion:
            if el.get_exponent() == exp:
                result.add_to_const(int(el.get_constant()))

        return result

    def greatest_exponent(self, equasion):
        max = 0
        for el in equasion:
            if max < el.get_exponent():
                max = el.get_exponent()

        return max

    def to_monomials(self, equasion):
        to_mono = []
        for el in equasion.split("+"):
            to_mono.append(Monomial(el))

        return to_mono


# p = Polynom("3x+4x^2")
q = Polynom("3x^2+4x+3")
print(q.__str__())
