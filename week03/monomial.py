class Monomial:

    def __init__(self, mono):
        if self.is_constant(mono):
            self.constant = (True, int(mono))
            return
        else:
            self.constant = (False, 0)
        self.mono = mono
        self.variable = "x"
        self.coef = self.take_coef()
        self.exponent = self.take_exponent()
        self.sign = ""

    def __str__(self):
        return "{sign}{coef}{var}^{exponent}".format(
            sign=self.get_sign(), coef=self.coef, var=self.variable, exponent=self.exponent)

    def get_sign(self):
        if self.sign is "-":
            return "-"
        else:
            return ""

    def is_constant(self, mono):
        try:
            int(mono)
            return True
        except ValueError:
            return False

    def take_coef(self):
        if self.mono[0] == self.variable:
            return ""
        else:
            return self.mono[:self.mono.index(self.variable)]

    def take_exponent(self):
        if "^" in self.mono[self.mono.index(self.variable):]:
            return self.mono[self.mono.index("^") + 1:]
        else:
            return ""

    def set_sign(self, sign):
        self.sign = sign

    def set_var(self, var):
        self.variable = var
