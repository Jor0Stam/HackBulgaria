def sudoku_solved(sudoku):
    o_to_n = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    status = True
    for i in sudoku:
        if check_for_numbers(i, o_to_n):
            print("Falied at 1")
            status = False

    for i in range(9):
        temp_list = [j[i]for j in sudoku]
        if check_for_numbers(temp_list, o_to_n):
            print("Falied at 2")
            status = False

    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            if check_box((i, j), sudoku, o_to_n):
                print("Falied at 3")
                status = False

    return status


def check_for_numbers(at, o_to_n):
    if o_to_n != set(at):
        return True

    return False


def check_box(at, sudoku, o_to_n):
    temp_list = [sudoku[at[0] + i][at[1] + j] for i in range(3) for j in range(3)]
    if set(temp_list) != o_to_n:
        return True

    return False


# False
sudokuF = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# True
sudokuT = [
    [4, 5, 2, 3, 8, 9, 7, 1, 6],
    [3, 8, 7, 4, 6, 1, 2, 9, 5],
    [6, 1, 9, 2, 5, 7, 3, 4, 8],
    [9, 3, 5, 1, 2, 6, 8, 7, 4],
    [7, 6, 4, 9, 3, 8, 5, 2, 1],
    [1, 2, 8, 5, 7, 4, 6, 3, 9],
    [5, 7, 1, 8, 9, 2, 4, 6, 3],
    [8, 9, 6, 7, 4, 3, 1, 5, 2],
    [2, 4, 3, 6, 1, 5, 9, 8, 7]]


def main():
    print(sudoku_solved(sudokuT))


if __name__ == "__main__":
    main()
