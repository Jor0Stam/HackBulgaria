import re


class Monomial:

    def __init__(self, mono):
        self.mono = mono
        self.constant = self.check_constant()
        self.exponent = self.check_exponent()
        self.variable = "x"
        self.is_constant = False
        self.check_is_constant()

    def __str__(self):
        return "{constant}{variable}{exponent}".format(
            constant=self.constant, variable=self.variable, exponent=self.exponent)

    def check_is_constant(self):
        try:
            int(self.mono)
            self.constant = self.mono
            self.variable = ""
            self.exponent = ""
            self.is_constant = True
        except ValueError:
            pass

    def check_constant(self):
        constant = ""
        try:
            constant = re.match("\w+x", self.mono).group(0)
            constant = constant[:-1]
        except AttributeError:
            constant = ""

        return constant

    def check_exponent(self):
        exponent = ""
        try:
            regEx = re.compile('\^(\w+)')
            exponent = regEx.search(self.mono).group(0)
        except AttributeError:
            exponent = ""

        return exponent
