def create_table(rows):
    return [input("Insert row {row}: ".format(row=i)) for i in range(rows)]


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


def palindrome(string):
    status = True

    for i in range(len(str(string)) // 2):
        if str(string)[i] != str(string)[len(str(string)) - 1 - i]:
            status = False
            break

    return status


def count_substrings(haystack, needle):
    # count = haystack.count(needle) one line solution
    count = 0
    for i in range(len(haystack) - len(needle)):
        count += int(haystack[i:i + len(needle)] == needle)

    return count


def sum_matrix(matrix):
    return sum([y for x in matrix for y in x])


def nan_expand(times):
    return times*"Not a " + "NaN"


def prime_factorization(n):
    prime_devisers = find_prime_devisers(n)
    return [(i, times_at_number(i, n)) for i in prime_devisers]


def times_at_number(sub_num, num):
    count = 0
    while num % sub_num == 0:
        num = num // sub_num
        count += 1

    return count


def find_prime_devisers(n):
    prime_devisers = []
    if prime(n):
        return []
    for i in range(2, n // 2 + 1):
        if prime(i) and n % i == 0:
            prime_devisers.append(i)

    return prime_devisers


def prime(n):
    if n == 2:
        return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def group(group):
    sorted_group = []
    temp_list = []
    group.append(None)
    for i in range(len(group) - 1):
        if group[i] == group[i + 1]:
            temp_list.append(group[i])
        else:
            if temp_list:
                temp_list.append(temp_list[0])
                sorted_group.append(temp_list)
            else:
                sorted_group.append([group[i]])
            temp_list = []

    return sorted_group


def max_consecutive(items):
    count = {}
    cnt = 0
    items.append(None)

    for i in range(1, len(items)):
        cnt += 1
        if items[i] == items[i - 1]:
            continue
        count[i] = cnt
        cnt = 0

    return max(value for key, value in count.items())


def main():
    # print(count_substrings("babababa", "baba"))
    # print(sum_matrix([ [0, 1, 2], [3, 4, 5], [6, 7, 8] ]) )
    # print(nan_expand(1))
    # print(prime_factorization(1000))
    print(group([1, 1, 1, 2, 3, 1, 1]))
    # print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
    # print(word_counter("asd", 3, 3))
    # pass


if __name__ == "__main__":
    main()
