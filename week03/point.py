class Point:

    def __init__(self, row, col, is_alive=False):
        self.row = row
        self.col = col
        self.is_alive = is_alive

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash(self.hash)

    def __str__(self):
        return "[{x}][{y}]".format(x=self.row, y=self.col)

    def get_elem(self):
        return (self.row, self.col)

    def get_status(self):
        return self.is_alive


class Matrix:

    def __init__(self, allive_cells, matrix_size):
        self.allive_cells = allive_cells
        self.matrix_size = max(matrix_size, 12)

    def __str__(self):
        to_p = []
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if (i, j) in self.allive_cells:
                    to_p.append("[" + str(u"\u25A0") + "]")
                else:
                    to_p.append("[" + str(u"\u25A1") + "]")
            to_p.append("\n")

        return "".join(to_p)
