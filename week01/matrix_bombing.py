from copy import deepcopy


def sum_it(m):
    result = 0
    for row in m:
        for el in row:
            result += el
    return result


def bomb_it(m, row, col):
    x = 0
    y = 1
    directions = [(var, varc) for var in range(-1, 2) for varc in range(-1, 2)]
    for el in directions:
        if el == (0, 0):
            continue
        if el[x] + row in range(len(m)) and el[y] + col in range(len(m[0])):
            m[el[x] + row][el[y] + col] = max(0, m[el[x] + row][el[y] + col] -
                                              m[row][col])
    return sum_it(m)


def matrix_bombing_plan(m):
    result = {}
    for row in range(len(m)):
        for col in range(len(m[0])):
            result[(row, col)] = bomb_it(deepcopy(m), row, col)
    return result


print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
