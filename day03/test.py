import unittest
from day3 import manhattan_disatance_from_1

class TestMethods(unittest.TestCase):

    def test_manhattan_disatance_from_1(self):
        self.assertEqual(manhattan_disatance_from_1(1), 0)
        self.assertEqual(manhattan_disatance_from_1(12), 3)
        self.assertEqual(manhattan_disatance_from_1(23), 2)
        self.assertEqual(manhattan_disatance_from_1(1024), 31)


if __name__ == '__main__':
    unittest.main()
