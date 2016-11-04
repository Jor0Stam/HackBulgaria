from collections import Counter


# A function for suming the digits of a number w
def sum_of_digits(number):
    sum_is = sum([int(x) for x in str(abs(number))])
    # sum = 0
    # if number < 0:
    #     number = (-1)*number
    # while (number):
    #     sum += number%10
    #     number = number//10

    return sum_is


# Create list with the digits of a number w
def to_digits(number):
    list_of_digits = []
    i = 1
    while number:
        list_of_digits.append(number % 10)
        number = number // 10
        i += 1

    list_of_digits.reverse()
    return list_of_digits


# Create number from array w
def to_number(digits):
    number = []
    for i in digits:
        number.append(str(i))

    return "".join(number)


# Count the vowels in a string w
def count_vowels(string):
    vowels = 0
    for char in string:
        if char in "aeiouyAEIOUY":
            vowels += 1

    return vowels


# Count the consonants in a string w
def count_consonants(string):
    consonants = 0
    for char in string:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonants += 1

    return consonants


# Check if a given number is prime w
def prime_number(number):
    status = "It's Prime!"
    for i in range(2, number // 2):
        if number % i == 0:
            status = "It's Not Prime!"

    return status


# Sum of the factorials of the digits in the number w
def fact_digits(n):
    sum = 0
    list_of_digits = to_digits(n)
    for i in list_of_digits:
        sum += fact(i)

    return sum


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# fibonacci sequince w
def fibonacci(number):
    list_of_fibonacci = []
    for i in range(1, number + 1):
        list_of_fibonacci.append(number_of_fibonaci(i))

    return to_number(list_of_fibonacci)


def number_of_fibonaci(number):
    if number in [1, 2]:
        return 1
    else:
        return number_of_fibonaci(number - 1) + number_of_fibonaci(number - 2)


# Check if a given string is palindrome w
def palindrome(string):
    status = "Palindrome"

    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            status = "Not Palindrome!"
            break

    return status


# Dictionary with all characters from a string w
def char_histogram(string):
    cnt = Counter()
    for char in string:
        cnt[char] += 1

    return cnt


def main():
    pass
    # print(sum_of_digits(-34))
    # print(to_digits(1234))
    # print(to_number([1, 22, 3, 54]))
    # print (count_vowels("Hello there :)"))
    # print(count_consonants(" as!124adssd"))
    # print(prime_number(6))
    # print(fact_digits(145))
    # print(fibonacci(10))
    # print(palindrome("sastsas"))
    # print(char_histogram("aaaAA!!"))


if __name__ == "__main__":
    main()
