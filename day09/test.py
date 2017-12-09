import unittest
from program import task1


def read(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()][0]


class TestMethods(unittest.TestCase):

    def test_task1(self):
        self.assertEqual(task1("{}")[1], 1)
        self.assertEqual(task1("{{{}}}")[1], 6)
        self.assertEqual(task1("{{},{}}")[1], 5)
        self.assertEqual(task1("{{{},{},{{}}}}")[1], 16)
        self.assertEqual(task1("{<a>,<a>,<a>,<a>}")[1], 1)
        self.assertEqual(task1("{{<ab>},{<ab>},{<ab>},{<ab>}}")[1], 9)
        self.assertEqual(task1("{{<!!>},{<!!>},{<!!>},{<!!>}}")[1], 9)
        self.assertEqual(task1("{{<a!>},{<a!>},{<a!>},{<ab>}}")[1], 3)
        self.assertEqual(task1(read("input.txt"))[1], 10800)

    def test_task2(self):
        self.assertEqual(task1("<>")[0], 0)
        self.assertEqual(task1("<random characters>")[0], 17)
        self.assertEqual(task1("<<<<>")[0], 3)
        self.assertEqual(task1("<{!>}>")[0], 2)
        self.assertEqual(task1("<!!>")[0], 0)
        self.assertEqual(task1("<!!!>>")[0], 0)
        self.assertEqual(task1('<{o"i!a,<{i<a>')[0], 10)
        self.assertEqual(task1(read("input.txt"))[0], 4522)

if __name__ == '__main__':
    unittest.main()
