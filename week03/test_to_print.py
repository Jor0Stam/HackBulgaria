import unittest
from to_print import GoL


class TestGol(unittest.TestCase):

    def setUp(self):
        self.pattern = GoL()

    def test_str(self):
        self.assertEqual(self.pattern.__str__(), "[1][2] [3][4]")

    def test_get_size(self):
        self.assertEqual(self.pattern.get_size(), 8)

    def test_in_matrix(self):
        self.assertTrue(self.pattern.in_matrix(self.pattern.coords[0], self.pattern.allive_cells[0]))


if __name__ == "__main__":
    unittest.main()
