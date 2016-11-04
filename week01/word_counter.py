from First_steps_in_Python import palindrome


def create_table(rows):
    return [input("Insert row {row}: ".format(row = i)) for i in range(rows)]


def check_for_word(word, check_here):
    return check_here.count(word) + check_here[::-1].count(word)


def check_diagonal_c(col, word, letters_table):
    diagonal = ""
    row = 0
    while(col < len(letters_table[0]) and row < len(letters_table)):
        diagonal += letters_table[row][col]
        row += 1
        col += 1

    return check_for_word(word, diagonal)


def check_diagonal_r(row, word, letters_table):
    diagonal = ""
    col = 0
    while(col < len(letters_table[0]) and row < len(letters_table)):
        diagonal += letters_table[row][col]
        row += 1
        col += 1

    return check_for_word(word, diagonal)


def reverse_h_table(letters_table):
    new_table = []
    for row in letters_table:
        new_table.append(row[::-1])

    return new_table


def word_counter(word, rows, columns):
    count = 0
    letters_table = create_table(rows)

    # checking rows
    for row in letters_table:
        count += check_for_word(word, row)

    # checking columns
    for col in range(columns):
        col_content = ""
        for row in letters_table:
            col_content += row[col]
        count += check_for_word(word, col_content)

    # checking left-right diagonals
    for col in range(1, columns - len(word) + 1):
        count += check_diagonal_c(col, word, letters_table)

    for row in range(len(letters_table) + 1):
        count += check_diagonal_r(row, word, letters_table)

    reversed_h_letters_table = reverse_h_table(letters_table)

    # checking right-left diagonals
    for col in range(1, columns - len(word) + 1):
        count += check_diagonal_c(col, word, reversed_h_letters_table)

    for row in range(len(reversed_h_letters_table) + 1):
        count += check_diagonal_r(row, word, reversed_h_letters_table)

    if palindrome(word):
        return count / 2
    else:
        return count


def main():
    print(word_counter("asd", 5, 5))


if __name__ == "__main__":
    main()
