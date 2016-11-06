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
