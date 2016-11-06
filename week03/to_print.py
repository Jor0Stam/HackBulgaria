import time


class GoL:

    def __init__(self):
        self.allive_cells = self.create_alive_cells()
        self.coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __str__(self):
        return " ".join([el.__str__() for el in self.allive_cells])

    def create_alive_cells(self):
        num_of_allive_cells = int(input("Input number of cells:"))
        cells = []
        for i in range(num_of_allive_cells):
            cell = input().split(" ")
            cells.append((int(cell[0]), int(cell[1])))

        return cells

    def get_size(self):
        try:
            return 2 * max([max(el) for el in self.allive_cells])
        except ValueError:
            return 0

    def iterate(self):
        temp = []
        for el in self.allive_cells:
            temp += self.still_alive(el)
        for el in self.allive_cells:
            temp += self.dead_alive(el, temp)

        self.allive_cells = list(set(temp))

    def still_alive(self, el):
        new_allive_cells = []
        for el in self.allive_cells:
            self.around_cell(el, new_allive_cells, [2, 3])

        return new_allive_cells

    def around_cell(self, cell, new_cells, condition):
        around_cell = 0
        for el in self.coords:
            if not self.in_matrix((el[0] + cell[0], el[1] + cell[1])):
                continue
            if (el[0] + cell[0], el[1] + cell[1]) in self.allive_cells:
                around_cell += 1

        if around_cell in condition:
            new_cells.append(cell)

    def dead_alive(self, el, elements):
        new_allive_cells = []
        for el in self.allive_cells:
            self.around_alive_cells(el, new_allive_cells)

        return new_allive_cells

    def around_alive_cells(self, cell, new_cells):
        for el in self.coords:
            if not self.in_matrix((el[0] + cell[0], el[1] + cell[1])):
                continue
            self.around_cell((el[0] + cell[0], el[1] + cell[1]), new_cells, [3])

    def in_matrix(self, el):
        return el[0] > 0 and el[0] < self.get_size() and el[1] > 0 and el[1] < self.get_size()


def main():
    a = GoL()
    while True:
        a.iterate()
        print(a)
        time.sleep(1)


if __name__ == "__main__":
    main()
