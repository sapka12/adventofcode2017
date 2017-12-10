import unittest
from program import task1, task2, to_ascii


def read(input_file):
    with open(input_file) as f:
        return [int(i) for i in [x.strip() for x in f.readlines()][0].split(",")]


class TestMethods(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(task1(5, [3, 4, 1, 5]), 12)
        self.assertEqual(task1(256, read("input.txt")), 4114)

    def test_ord(self):
        self.assertEqual(to_ascii("1,2,3"), [int(i) for i in "49,44,50,44,51".split(",")])

    def test_tas2(self):
        self.assertEqual(task2(""), "a2582a3a0e66e6e86e3812dcb672a272")
        self.assertEqual(task2("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")
        self.assertEqual(task2("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")
        self.assertEqual(task2("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")


if __name__ == '__main__':
    unittest.main()
