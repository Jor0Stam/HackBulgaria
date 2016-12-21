import sys


class Func:

    def __init__(self, expresion):
        self.name = expresion.split(" ")[0]
        self.dom = expresion.split(" ")[2]
        self.range = expresion.split(" ")[4].rstrip('\n')

    def __str__(self):
        return "{n}::{d}->{r}".format(n=self.name, d=self.dom, r=self.range)

    def __repr__(self):
        return "{n}::{d}->{r}".format(n=self.name, d=self.dom, r=self.range)


def check_composition(comp, funcs):
    formated_comp = []
    for el in comp:
        formated_comp.append(funcs[el].range)
        formated_comp.append(funcs[el].dom)
    for i in range(1, len(formated_comp) - 1, 2):
        if formated_comp[i] != formated_comp[i + 1]:
            return False
    return True


def main():
    inpt = list(sys.stdin)
    funcs = {}
    for i in range(len(inpt) - 2):
        funcs[Func(inpt[i]).name] = (Func(inpt[i]))
    print(check_composition(inpt[-1].split(" . "), funcs))


if __name__ == "__main__":
    main()
