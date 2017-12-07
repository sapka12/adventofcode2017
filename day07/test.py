import unittest
from program import task1, task2


def read_input():
    with open("input.txt") as f:
        strings = [x.strip() for x in f.readlines()]
        nums_as_strings = strings[0].split('\t')
        return [int(numeric_string) for numeric_string in nums_as_strings]


class TestMethods(unittest.TestCase):


    def test_task1(self):
        self.assertEqual(task1("example.txt"), "tknk")
        self.assertEqual(task1("input.txt"), "rqwgj")


    # def test_task2(self):
    #     self.assertEqual(task2([0, 2, 7, 0]), 4)
    #     self.assertEqual(task2(read_input()), 2793)


if __name__ == '__main__':
    unittest.main()
