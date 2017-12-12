import unittest
import math
from program import task1, task2


def read(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()][0].split(",")


class TestMethods(unittest.TestCase):

    def test_task1(self):
		self.assertEquals(task1("ne,ne,ne".split(",")), 3)
		self.assertEquals(task1("ne,ne,sw,sw".split(",")), 0)
		self.assertEquals(task1("ne,ne,s,s".split(",")), 2)
		self.assertEquals(task1("se,sw,se,sw,sw".split(",")), 3)
		# self.assertEquals(task1(read("input.txt")), 773)

    def test_task2(self):
        self.assertEquals(task2("ne,ne,ne".split(",")), 3)
        self.assertEquals(task2("ne,ne,sw,sw".split(",")), 2)
        self.assertEquals(task2("ne,ne,s,s".split(",")), 2)
        self.assertEquals(task2("se,sw,se,sw,sw".split(",")), 3)
        self.assertEquals(task2("n,n,s,s".split(",")), 2)
        self.assertEquals(task2(read("input.txt")), 0)

if __name__ == '__main__':
    unittest.main()
