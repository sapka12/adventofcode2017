import unittest
from program import task1, task2


def read(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()]


def get_map(input_file):
    return {int(line.split(": ")[0]): int(line.split(": ")[1]) for line in read(input_file)}


class TestMethods(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(task1(get_map("test.txt")), 24)
        self.assertEqual(task1(get_map("input.txt")), 648)

    def test_task2(self):
        self.assertEqual(task2(get_map("test.txt")), 10)
        self.assertEquals(task2(get_map("input.txt")), 3933124)


if __name__ == '__main__':
    unittest.main()
