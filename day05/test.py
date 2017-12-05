import unittest
from program import task1, task2


def read_input():
    with open("input.txt") as f:
        strings = [x.strip() for x in f.readlines()]
        return [int(numeric_string) for numeric_string in strings]


class TestMethods(unittest.TestCase):


    def test_task1(self):
        self.assertEqual(task1([0, 3, 0, 1, -3]), 5)
        self.assertEqual(task1(read_input()), 343467)


    def test_task2(self):
        self.assertEqual(task2([0, 3, 0, 1, -3]), 10)
        self.assertEqual(task2(read_input()), 24774780)


if __name__ == '__main__':
    unittest.main()
