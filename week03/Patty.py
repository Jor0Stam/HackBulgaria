from turtle import *
import time


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


def curvemove():
    for i in range(200):
        right(1)
        forward(1)


points = []
h_points = []


def Patty(points):
    # P
    for i in range(10):
        points.append((i, 0))

    points.append((0, 1))
    points.append((0, 2))
    points.append((1, 3))
    points.append((2, 3))
    points.append((3, 2))
    points.append((4, 1))

    # A
    for i in range(2, 10):
        points.append((i, 5))

    for i in range(2, 10):
        points.append((i, 9))

    points.append((1, 6))
    points.append((0, 7))
    points.append((1, 8))

    for i in range(5, 9):
        points.append((5, i))

    # T
    for i in range(11, 17):
        points.append((0, i))

    for i in range(1, 10):
        points.append((i, 13))
        points.append((i, 14))

    # T
    for i in range(18, 24):
        points.append((0, i))

    for i in range(1, 10):
        points.append((i, 20))
        points.append((i, 21))

    # Y
    for i in range(4):
        points.append((i, 25))

    for i in range(9):
        points.append((i, 28))

    points.append((4, 26))
    points.append((4, 27))
    points.append((9, 26))
    points.append((9, 27))
    points.append((8, 25))

    # !
    for i in range(8):
        points.append((i, 30))

    points.append((9, 30))

    return points


print(Matrix(Patty(points), 32))

time.sleep(2)

color('red', 'pink')
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()

time.sleep(15)
