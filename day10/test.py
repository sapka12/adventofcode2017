import unittest
from program import task1


def read(input_file):
    with open(input_file) as f:
        return [int(i) for i in [x.strip() for x in f.readlines()][0].split(",")]


class TestMethods(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(task1(5, [3, 4, 1, 5]), 12)
        self.assertEqual(task1(256, read("input.txt")), 4114)


if __name__ == '__main__':
    unittest.main()
