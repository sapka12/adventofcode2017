import unittest
from program import task1, task2, to_ascii


def read_str(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()][0]


def read(input_file):
    return [int(i) for i in read_str(input_file).split(",")]


class TestMethods(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(task1(5, [3, 4, 1, 5]), 12)
        self.assertEqual(task1(256, read("input.txt")), 4114)

    def test_tas2(self):
        self.assertEqual(task2(""), "a2582a3a0e66e6e86e3812dcb672a272")
        self.assertEqual(task2("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")
        self.assertEqual(task2("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")
        self.assertEqual(task2("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")
        self.assertEqual(task2(read_str("input.txt")), "2f8c3d2100fdd57cec130d928b0fd2dd")


if __name__ == '__main__':
    unittest.main()
