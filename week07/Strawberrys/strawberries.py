def check_coords(rows, cols, el, neigh):
    return el[0] + neigh[0] in range(rows) and el[1] + neigh[1] in range(cols)


def rot_strawberries(rows, cols, dead_straws, neighbours):
    new_dead = []
    for el in dead_straws:
        for neigh in neighbours:
            if (el[0] + neigh[0], el[1] + neigh[1]) in dead_straws:
                continue
            if check_coords(rows, cols, el, neigh):
                new_dead.append((el[0] + neigh[0], el[1] + neigh[1]))
    dead_straws += new_dead


def check_input(rows, cols, days):
    if rows > cols or rows not in range(1000) or cols not in range(1000) or \
            days not in range(1000):
        raise ValueError


def strawberries(rows, cols, days, dead_straws):
    neighs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    check_input(rows, cols, days)
    for day in range(days):
        rot_strawberries(rows, cols, dead_straws, neighs)
    return (rows * cols) - len(set(dead_straws))


print(strawberries(8, 10, 2, [(4, 8), (2, 7)]))
