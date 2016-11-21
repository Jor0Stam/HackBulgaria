from collections import Counter
from copy import deepcopy


# Dictionary with all characters from a string w
def char_histogram(string):
    cnt = Counter()
    for char in string:
        cnt[char] += 1

    return cnt


# Checks if two strings are anagrams
def anagram(string_1, string_2):
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    status = "ANAGRAMS"
    if char_histogram(string_1) != char_histogram(string_2):
        status = "NOT ANAGRAMS"

    if string_1 == "Krisko" or string_2 == "Kilata":
        print("PLz stop hurtin' our ears Majka :/")

    return status


# "a smart GPS software." or how many times we need to refill our tank
def gas_stations(distance, tank_size, stations):
    if stations[0] > tank_size:
        return "You aint going anywhere!"
    stations.append(distance)
    size = tank_size - stations[0]
    result = []
    for i in range(1, len(stations)):
        diff = stations[i] - stations[i - 1]
        if (size < diff):
            result.append(stations[i - 1])
            size = tank_size
        size = size - diff

    return result


def prime_number(number):
    status = True
    for i in range(2, number // 2):
        if number % i == 0:
            status = False

    return status


# A function giving you the prime goldbach numbers for n
def goldbach(n):
    prime_couples = []
    for i in range(n // 2 + 1):
        if prime_number(i):
            if prime_number(n - i):
                prime_couples.append((i, n - i))

    return prime_couples


def reduce_file_path(path):  # NOT WORKING !
    path = path.split("/")
    r_path = ''.join(path)
    go_back = r_path.count('..')
    path = [x for x in path if x not in ['..', '.', '']]
    path = ''.join(["/" + path[x] for x in range(len(path) - go_back)])
    if not path:
        path += "/"

    return path


def to_digits(number):
    return[int(x) for x in str(number)]


def is_credit_card_valid(number):
    list_of_digits = to_digits(number)
    for i in range(1, len(list_of_digits), + 2):
        list_of_digits[i] = list_of_digits[i] * 2
    if sum(x for x in list_of_digits) % 10 == 0:
        return "Number Invalid !"
    else:
        return "Valid Number !"


def sum_matrix(m, rows, columns):
    sum = 0
    for i in range(rows):
        for j in range(columns):
            sum += m[i][j]
    return sum


def bomb_it(row, column, new_m):
    # corner 1
    if row == 0 and column == 0:
        new_m[1][0] = max(new_m[1][0] - m[row][column], 0)
        new_m[0][1] = max(new_m[0][1] - m[row][column], 0)
        new_m[1][1] = max(new_m[1][1] - m[row][column], 0)
    # corner 2
    elif row == 0 and column == m[-1][1] - 1:
        new_m[row][column - 1] = max(new_m[row][column - 1] - m[row][column], 0)
        new_m[row + 1][column - 1] = max(new_m[row + 1][column - 1] - m[row][column], 0)
        new_m[row + 1][column] = max(new_m[row + 1][column] - m[row][column], 0)
    # corner 3
    elif row == m[-1][0] - 1 and column == m[-1][1] - 1:
        new_m[row][column - 1] = max(new_m[row][column - 1] - m[row][column], 0)
        new_m[row - 1][column] = max(new_m[row - 1][column] - m[row][column], 0)
        new_m[row - 1][column - 1] = max(new_m[row - 1][column - 1] - m[row][column], 0)
    # corner 4
    elif row == m[-1][0] - 1 and column == 0:
        new_m[row - 1][column] = max(new_m[row - 1][column] - m[row][column], 0)
        new_m[row - 1][column + 1] = max(new_m[row - 1][column + 1] - m[row][column], 0)
        new_m[row][column + 1] = max(new_m[row][column + 1] - m[row][column], 0)
    # edge 1
    elif row == 0 and column in range(1, m[-1][1] - 1):
        new_m[row][column - 1] = max(new_m[row][column - 1] - m[row][column], 0)
        new_m[row + 1][column - 1] = max(new_m[row + 1][column - 1] - m[row][column], 0)
        new_m[row + 1][column] = max(new_m[row + 1][column] - m[row][column], 0)
        new_m[row + 1][column + 1] = max(new_m[row + 1][column + 1] - m[row][column], 0)
        new_m[row][column + 1] = max(new_m[row][column + 1] - m[row][column], 0)
    # edge 2
    elif row in range(1, m[-1][0] - 1) and column == m[-1][1] - 1:
        new_m[row - 1][column] = max(new_m[row - 1][column] - m[row][column], 0)
        new_m[row - 1][column - 1] = max(new_m[row - 1][column - 1] - m[row][column], 0)
        new_m[row][column - 1] = max(new_m[row][column - 1] - m[row][column], 0)
        new_m[row + 1][column - 1] = max(new_m[row + 1][column - 1] - m[row][column], 0)
        new_m[row + 1][column] = max(new_m[row + 1][column] - m[row][column], 0)
    # edge 3
    elif row == m[-1][0] - 1 and column in range(1, m[-1][1] - 1):
        new_m[row][column - 1] = max(new_m[row][column - 1] - m[row][column], 0)
        new_m[row - 1][column - 1] = max(new_m[row - 1][column - 1] - m[row][column], 0)
        new_m[row - 1][column] = max(new_m[row - 1][column] - m[row][column], 0)
        new_m[row - 1][column + 1] = max(new_m[row - 1][column + 1] - m[row][column], 0)
        new_m[row][column + 1] = max(new_m[row][column + 1] - m[row][column], 0)
    # edge 4
    elif row in range(1, m[-1][0] - 1) and column == 0:
        new_m[row - 1][column] = max(new_m[row - 1][column] - m[row][column], 0)
        new_m[row - 1][column + 1] = max(new_m[row - 1][column + 1] - m[row][column], 0)
        new_m[row][column + 1] = max(new_m[row][column + 1] - m[row][column], 0)
        new_m[row + 1][column + 1] = max(new_m[row + 1][column + 1] - m[row][column], 0)
        new_m[row + 1][column] = max(new_m[row + 1][column] - m[row][column], 0)
    # center
    elif row not in [0, m[-1][0] - 1] and column not in [0, m[-1][1] - 1]:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                new_m[row + i][column + j] = max(new_m[row + i][column + j] - m[row][column], 0)
    else:
        pass

    return new_m


def matrix_bombing_plan(m):
    after_bombing = {}
    rows = m[-1][0]
    columns = m[-1][1]
    new_m = []
    for i in range(rows):
        for j in range(columns):
            new_m = list(bomb_it(i, j, deepcopy(m)))
            after_bombing[(i, j)] = sum_matrix(new_m, m[-1][0], m[-1][1])

    return after_bombing

#  (0, 0): 42,
#  (0, 1): 36,
#  (0, 2): 37,
#  (1, 0): 30,
#  (1, 1): 15,
#  (1, 2): 23,
#  (2, 0): 29,
#  (2, 1): 15,
#  (2, 2): 26}


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [3, 3]]


def main():
    pass
    # print(char_histogram("aaaAA!!"))
    # print(anagram("TOP_CODER", "COTO_PRODE"))
    # print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
    # print(goldbach(10))
    # print(reduce_file_path("/asda/asd//asd//..asd/.."))
    # print(is_credit_card_valid(1234112))
    # print(matrix_bombing_plan(matrix))


if __name__ == "__main__":
    main()
