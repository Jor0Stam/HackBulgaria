import sys
from monomial import Monomial


class Polynom:

    def __init__(self):
        self.variable = sys.argv[1]
        self.polynom = sys.argv[2]
        self.polynom = self.format_polynom()
        #self.first_derivativ = self.diferentiate()

    def format_polynom(self):
        good_polynom = []
        formated = self.polynom.split("+")
        ["x2", "x"]
        for sub in formated:
            if "-" in sub:
                new_sub = sub.split("-")
                formated.insert(formated.index(list(sub)), new_sub[0])
            else:
                good_polynom.append(Monomial(sub).set_sign("+"))
        print(formated)

    # def diferentiate(self):
    #     diferential = ""
    #     coef = ""
    #     exponent = ""

    #     for i in self.polynom:
    #         if i in ["+", "-"]:
    #             diferential += " {operand} ".format(operand=i)
    #         else:
    #             # exponent = self.take_exponent(i[i.index(self.variable):])
    #             coef = self.create_coef(i[:i.index(self.variable)], exponent)
    #             diferential += "{coef}{var}{exponent}".format(coef=coef, var=self.variable, exponent=exponent)

    #     return diferential

    # def take_exponent(self, exponent):
    #     if exponent[0] == "^":
    #         return "^" + (int(exponent[0:]) - 1)
    #     else:
    #         return ""

    # def create_coef(self, coef, exponent):
    #     if exponent == "":
    #         return coef
    #     else:
    #         return coef * int(exponent[0:])

    def __str__(self):
        return "This equasion is {equasion}".format(equasion="".join(self.polynom))

    # def get_diferential(self):
    #     return "The derivative of f(x) = {equasion} is:\nf'(x) = {derivativ}".format(
    #         equasion="".join(self.polynom), derivativ=self.first_derivativ)
