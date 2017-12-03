import unittest
from day3 import manhattan_disatance_from_1, part2

class TestMethods(unittest.TestCase):

    def test_manhattan_disatance_from_1(self):
        self.assertEqual(manhattan_disatance_from_1(1), 0)
        self.assertEqual(manhattan_disatance_from_1(12), 3)
        self.assertEqual(manhattan_disatance_from_1(23), 2)
        self.assertEqual(manhattan_disatance_from_1(1024), 31)
        self.assertEqual(manhattan_disatance_from_1(361527), 326)


    def test_task2(self):
        self.assertEqual(part2(1), 2)
        self.assertEqual(part2(2), 4)
        self.assertEqual(part2(3), 4)
        self.assertEqual(part2(4), 5)
        self.assertEqual(part2(100), 122)
        self.assertEqual(part2(700), 747)
        self.assertEqual(part2(361527), 363010)


if __name__ == '__main__':
    unittest.main()
