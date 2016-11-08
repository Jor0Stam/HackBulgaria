import unittest
from Polynomials import Polynom
from Monomials import Monomial


class TestMonomial(unittest.TestCase):

    def setUp(self):
        self.testMono = Monomial("2x^3")

    def test_constant(self):
        self.temp_mono = Monomial("x^4")
        self.assertEqual(self.temp_mono.constant, "")
        self.assertEqual(self.testMono.constant, "2")

    def test_exponent(self):
        self.temp_mono = Monomial("3x")
        self.assertEqual(self.testMono.exponent, "^3")
        self.assertEqual(self.temp_mono.exponent, "")

    def test_get_exponent(self):
        self.assertEqual(self.testMono.get_exponent(), 3)

    def test_add_to_const(self):
        self.assertTrue(self.testMono.add_to_const(""))
        self.assertTrue(self.testMono.add_to_const("13"))


class TestPolynomial(unittest.TestCase):

    def setUp(self):
        self.test_poly = Polynom("2x^2+3x+5")

    def test_get_first_derivative(self):
        self.assertEqual(self.test_poly.get_first_derivativ(), "4x+3")

if __name__ == "__main__":
    unittest.main()
