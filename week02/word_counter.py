def word_counter(search_word, rows, columns, words_matr):
    count = 0
    if len(search_word) > rows or len(search_word) > columns:
        return "Your matrix should be bigger in order to find the word :)"

    for row in range(rows):
        count += check_row(search_word, row, words_matr)

    for col in range(columns):
        count += check_col(search_word, col, words_matr)

    for row in range(rows - len(search_word) + 1):
        for col in range(columns - len(search_word) + 1):
            # check_diagonals(search_word, row, col, words_matr)
            print((row, col))

    return count


def check_row(search_word, row, words_matr):
    temp_row = ''.join([x for x in words_matr[row]])
    return temp_row.count(search_word)


def check_col(search_word, col, words_matr):
    temp_row = ''.join([x[col] for x in words_matr])
    return temp_row.count(search_word)


def check_diagonals(search_word, row, col, words_matr):
    pass
    #temp_row = ''.join([x in ])


def main():
    print(word_counter("ivan", 5, 5, ["asdi", "asdv", "asda", "ivan"]))


if __name__ == "__main__":
    main()
