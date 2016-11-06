import unittest
from Polynomials import Polynom
from Monomials import Monomial


class TestMonomial(unittest.TestCase):

    def setUp(self):
        self.testMono = Monomial("3x^4")

    def test_constant(self):
        self.temp_mono = Monomial("x^4")
        self.assertEqual(self.temp_mono.constant, "")
        self.assertEqual(self.testMono.constant, "3")

    def test_exponent(self):
        self.temp_mono = Monomial("3x")
        self.assertEqual(self.testMono.exponent, "^4")
        self.assertEqual(self.temp_mono.exponent, "")


if __name__ == "__main__":
    unittest.main()
