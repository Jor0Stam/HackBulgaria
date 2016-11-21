import unittest
from First_steps_in_Python import *


class Test_sum_of_digits(unittest.TestCase):

    def setUp(self):
        self.num1 = 1 + 2 + 3
        self.num2 = 1 + 2 + 3 + 0 + 3

    def test_sum(self):
        self.assertEqual(sum_of_digits(-123), self.num1)
        self.assertEqual(sum_of_digits(12303), self.num2)


class Test_to_digits(unittest.TestCase):

    def setUp(self):
        self.num1 = [1, 2, 3]
        self.num2 = [9, 9, 9, 9]

    def test_to_digits(self):
        self.assertEqual(to_digits(123), self.num1)
        self.assertEqual(to_digits(9999), self.num2)


class Test_to_number(unittest.TestCase):

    def setUp(self):
        self.test_var1 = 123
        self.test_var2 = 90909

    def test_to_num(self):
        self.assertEqual(to_number([1, 2, 3]), self.test_var1)
        self.assertEqual(to_number([9, 0, 9, 0, 9]), self.test_var2)


class Test_count_vowels(unittest.TestCase):

    def setUp(self):
        self.test_var1 = 6
        self.test_var2 = 10

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello, My Name is :)"), self.test_var1)
        self.assertEqual(count_vowels("Hello, My Name is Georginjo:)"), self.test_var2)


class Test_count_consonants(unittest.TestCase):

    def setUp(self):
        self.test_var1 = 7
        self.test_var2 = 22

    def test_count_consonants(self):
        self.assertEqual(count_consonants("Hello Baba TT!"), self.test_var1)
        self.assertEqual(count_consonants("My Name is WHAT? Thucka Thchuka - SLim SHady!"), self.test_var2)


class Test_prime_number(unittest.TestCase):

    def setUp(self):
        self.prime1 = 7
        self.not_prime1 = 10

    def test_prime_number(self):
        self.assertFalse(prime_number(self.not_prime1))
        self.assertTrue(prime_number(self.prime1))


class Test_fact_digits(unittest.TestCase):

    def setUp(self):
        self.sum_of_facts_101 = 3
        self.sum_of_facts_51243 = 153
        self.fact_of_0 = 1
        self.fact_of_8 = 40320

    def test_fact_digits(self):
        self.assertEqual(fact_digits(101), self.sum_of_facts_101)
        self.assertEqual(fact_digits(51243), self.sum_of_facts_51243)

    def test_fact(self):
        self.assertEqual(fact(0), self.fact_of_0)
        self.assertEqual(fact(8), self.fact_of_8)


class Test_fibonacci_numbers(unittest.TestCase):

    def setUp(self):
        self.first_ten_fibonaci_nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.the16th_fibonacci_num = 987

    def test_fibonaci(self):
        self.assertEqual(fibonacci(10), self.first_ten_fibonaci_nums)

    def test_fibonaci_num(self):
        self.assertEqual(number_of_fibonaci(16), self.the16th_fibonacci_num)


class Test_Palindrome(unittest.TestCase):

    def setUp(self):
        self.palindrome1 = "asddsa"
        self.palindrome2 = "babab"
        self.not_palindrom1 = "asd"
        self.not_palindrom2 = "qwetytewqq"

    def test_palyndrom(self):
        self.assertTrue(palindrome(self.palindrome1))
        self.assertTrue(palindrome(self.palindrome2))
        self.assertFalse(palindrome(self.not_palindrom1))
        self.assertFalse(palindrome(self.not_palindrom2))


class Test_char_histogram(unittest.TestCase):

    def setup(self):
        self.str1 = "cabcbc"
        self.str2 = "!@w!@1!@1@@"

    def test_char_histogram(self):
        self.assertEqual(char_histogram(self.str1), {"a": 1, "b": 2, "c": 3})
        self.assertEqual(char_histogram(self.str2), {"!": 2, "@": 4, "w": 1, "1": 3})


if __name__ == "__main__":
    unittest.main()
