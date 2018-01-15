import unittest
from program import task1, task2


def read_moves(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()][0].split(",")


class TestMethods(unittest.TestCase):

    def test_task1(self):
        self.assertEqual(task1(["s1"], list("abcde")), "eabcd")
        self.assertEqual(task1(["x3/4"], list("abcde")), "abced")
        self.assertEqual(task1(["pe/b"], list("abcde")), "aecdb")
        self.assertEqual(task1(["s1", "x3/4", "pe/b"], list("abcde")), "baedc")
        self.assertEqual(task1(read_moves("input.txt"), list("abcdefghijklmnop")), "bijankplfgmeodhc")

    def test_do_permutation(self):
        self.assertEqual(task2(read_moves("input.txt"), list("abcdefghijklmnop"), 1000000000), "bpjahknliomefdgc")

if __name__ == '__main__':
    unittest.main()
