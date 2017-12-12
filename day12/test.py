import unittest
from program import task1, task2


def read(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()]


def get_map(input_file):
    return {
        int(line.split(" <-> ")[0]): [int(i) for i in line.split(" <-> ")[1].split(", ")]
        for line in read(input_file)
    }


class TestMethods(unittest.TestCase):
    def test_task1(self):
        self.assertEquals(task1(get_map("test.txt")), 6)
        self.assertEquals(task1(get_map("input.txt")), 130)

    def test_task2(self):
        self.assertEquals(task2(get_map("test.txt")), 2)
        self.assertEquals(task2(get_map("input.txt")), 189)


if __name__ == '__main__':
    unittest.main()
