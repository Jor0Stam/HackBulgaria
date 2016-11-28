import re


def palindrome(i):
    for el in range((len(i))):
        if not i[el] == i[-1 - el]:
            return False
    return True


def to_number(i):
    result = ""
    for el in i:
        result += str(el)
    return int(result)


def is_number_balanced(n):
    if len(str(n)) == 1:
        return True
    list_num = [int(num) for num in str(n)]
    len_list = len(list_num) // 2
    if len(list_num) % 2 == 0:
        sumL = sum(list_num[i] for i in range(len_list))
        sumR = sum(list_num[i] for i in range(len_list, len(list_num)))
        print("even")
        print(sumL)
        print(sumR)
        return sumL == sumR
    else:
        sumL = sum(list_num[i] for i in range(len_list))
        sumR = sum(list_num[i] for i in range(len_list + 1, len(list_num)))
        print(sumL)
        print(sumR)
        return sumL == sumR


def increasing_or_decreasing(seq):
    result = "False !"
    up = [1, "Up!"]
    down = [1, "Down!"]
    for i in range(len(seq) - 1):
        if seq[i] < seq[i + 1]:
            up[0] = 1
        else:
            up[1] = "False !"
        if seq[i] > seq[i + 1]:
            down[0] = 1
        else:
            down[1] = "False !"
    if up[1] != "False !" or down[1] != "False !":
        if up[1] == "False !":
            result = down[1]
        else:
            result = up[1]
    if result == "False !":
        return False
    return result


def get_largest_palindrome(n):
    for i in range(n - 1, 0, -1):
        if palindrome(str(i)):
            return i


def sum_of_numbers(st):
    list_of_numbers = re.findall('\d+', st)
    return sum(int((i)) for i in list_of_numbers)


def birthday_ranges(birthdays, ranges):
    dict = {}
    first_time_here = 1
    for i in range(len(ranges)):
        for el in birthdays:
            if el >= ranges[i][0] and el <= ranges[i][1]:
                if first_time_here == 1:
                    dict[i] = 1
                    first_time_here = 0
                else:
                    dict[i] += 1
        if i not in dict.keys():
            dict[i] = 0
        first_time_here = 1
    return [value for value in dict.values()]


def numbers_to_message(pressed_sequence):
    letters_list = list_of_letters()
    dict_nums = dict_numbers_to_letters(letters_list)

    return translate_from_nokia(pressed_sequence, dict_nums)


def list_of_letters():
    letters = []
    for index in range(97, 123):
        letters.append(chr(index))

    return letters


def dict_numbers_to_letters(letters):
    dict_letters = {}
    nums = [2, 22, 222, 3, 33, 333, 4, 44, 444, 5, 55, 555, 6, 66, 666, 7, 77,
            777, 7777, 8, 88, 888, 9, 99, 999, 9999]
    index = 0
    for i in nums:
        dict_letters[i] = letters[index]
        index += 1
    dict_letters[-1] = "0"
    dict_letters[0] = " "
    dict_letters[1] = "1"
    return dict_letters


def translate_from_nokia(mssg, dict_nums):
    decoded_mssg = ""
    capital = False
    terminating_zero = None
    mssg.append(terminating_zero)

    key_holder = []
    for i in range(len(mssg) - 1):
        key_holder.append(mssg[i])
        if mssg[i] == mssg[i + 1]:
            continue
        elif mssg[i] is 0:
            decoded_mssg += " "
            key_holder = []
        elif mssg[i] is -1:
            key_holder = []
        elif mssg[i] is 1:
            capital = True
            key_holder = []
        else:
            key_holder = mod_letter(key_holder, dict_nums)
            if capital:
                decoded_mssg += dict_nums[int(to_number(key_holder))].upper()
                capital = False
            else:
                decoded_mssg += dict_nums[int(to_number(key_holder))]
            key_holder = []

    return decoded_mssg


def mod_letter(key_holder, dict_nums):
    qudaricals = [7, 9]
    if key_holder[0] in qudaricals and len(key_holder) > 4:
        return [key_holder[i] for i in range(len(key_holder) % 4)]
    elif len(key_holder) > 3:
        return [key_holder[i] for i in range(len(key_holder) % 3)]
    return key_holder


def dict_letters_to_numbers(letters):
    dict_letters = {}
    nums = [2, 22, 222, 3, 33, 333, 4, 44, 444, 5, 55, 555, 6, 66, 666, 7, 77,
            777, 7777, 8, 88, 888, 9, 99, 999, 9999]
    index = 0
    for i in letters:
        dict_letters[i] = nums[index]
        index += 1
    dict_letters[" "] = 0

    return dict_letters


def message_to_numbers(mssg):
    letters_list = list_of_letters()
    dict_letters = dict_letters_to_numbers(letters_list)

    return translate_to_nokia(mssg, dict_letters)


def to_list(i):
    return [int(el) for el in str(i)]


def translate_to_nokia(mssg, dict_letters):
    decoded_mssg = []

    for symb in mssg:
        if symb.isupper():
            if decoded_mssg:
                if decoded_mssg[-1] == to_list(dict_letters[symb.lower()])[0]:
                    decoded_mssg.append(-1)
            decoded_mssg.append(1)
            decoded_mssg.extend(to_list(dict_letters[symb.lower()]))
        else:
            if decoded_mssg:
                if decoded_mssg[-1] == to_list(dict_letters[symb])[0]:
                    decoded_mssg.append(-1)
            decoded_mssg.extend(to_list(dict_letters[symb]))

    return decoded_mssg


def main():
    print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))


if __name__ == "__main__":
    main()
