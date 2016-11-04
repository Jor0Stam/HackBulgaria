from word_counter import word_counter


def count_substrings(haystack, needle):
    # count = haystack.count(needle) one line solution
    count = 0
    for i in range(len(haystack) - len(needle)):
        count += int(haystack[i:i + len(needle)] == needle)

    return count


def sum_matrix(matrix):
    return sum([y for x in matrix for y in x])


def nan_expand(times):
    result = ""
    for i in range(times + 1):
        if times == 0:
            break
        if i == 1:
            result = "Nan"
        result = "Not a " + result

    return result


def prime_factorization(n):
    prime_devisers = find_prime_devisers(n)
    return [(i, times_at_number(i, n)) for i in prime_devisers]


def times_at_number(sub_num, num):
    count = 0
    while num % sub_num == 0:
        sub_num = sub_num**sub_num
        count += 1

    return count


def find_prime_devisers(n):
    prime_devisers = [1]
    if prime_number(n):
        return [1, n]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            prime_devisers.append(i)
    prime_devisers.append(n)

    return prime_devisers


def group(group):
    sorted_group = []
    temp_list = []
    for i in range(len(group)):
        if group[i] == group[i - 1]:
            temp_list.append(group[i])
            if i == len(group) - 1:
                sorted_group.append(temp_list)
        else:
            if temp_list:
                sorted_group.append(temp_list)
            sorted_group.append([group[i]])
            temp_list = []

    return sorted_group


def max_consecutive(items):
    count = {}

    for i in items:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return max(value for key, value in count.items())


def main():
    pass
    # print(count_substrings("babababa", "baba"))
    # print(sum_matrix([ [0, 1, 2], [3, 4, 5], [6, 7, 8] ]) )
    # print(nan_expand(1))
    # print(prime_factorization(100))
    # print(group([1, 1, 1, 2, 3, 1, 1]))
    # print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
    # print(word_counter("asd", 3, 3))  # "ivan", "evnh", "inav", "mvvn", "qrit"


if __name__ == "__main__":
    main()
