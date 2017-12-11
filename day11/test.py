import unittest
import math
from program import task1, task2


def read_str(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()][0]


def read(input_file):
    return [int(i) for i in read_str(input_file).split(",")]


class TestMethods(unittest.TestCase):
    def test_task1(self):
		self.assertEquals(task1("ne,ne,ne".split(",")), 3)
		self.assertEquals(task1("ne,ne,sw,sw".split(",")), 0)
		self.assertEquals(task1("ne,ne,s,s".split(",")), 2)
		self.assertEquals(task1("se,sw,se,sw,sw".split(",")), 3)


if __name__ == '__main__':
    unittest.main()
