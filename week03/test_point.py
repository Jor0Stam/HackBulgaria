from point import Point
import unittest


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.point = Point(1, 2, True)

    def test_eq(self):
        temp_point = Point(1, 2)
        self.assertEqual(self.point, temp_point)

    def test_get_elem(self):
        self.assertEqual(self.point.get_elem(), (1, 2))

    def test_get_status(self):
        self.assertEqual(self.point.get_status(), True)


if __name__ == "__main__":
    unittest.main()
