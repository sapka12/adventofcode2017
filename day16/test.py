import unittest
from program import task1, task2, exchange, spin, partner


def read_moves(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()][0].split(",")


class TestMethods(unittest.TestCase):


    # def test_task1_spin(self):
    #     self.assertEqual(task1(["s1"], "abcde"), "eabcd")
    #
    # def test_task1_spin1(self):
    #     self.assertEqual(task1(["s-4"], "abcde"), "eabcd")
    #
    # def test_task1_spin2(self):
    #     self.assertEqual(task1(["s10"], "abcde"), "abcde")
    #
    # def test_task1_exchange(self):
    #     self.assertEqual(task1(["s1", "x3/4"], "abcde"), "eabdc")
    #
    # def test_task1_partner(self):
    #     self.assertEqual(task1(["s1", "x3/4", "pe/b"], "abcde"), "baedc")
    #
    def test_task1(self):
        inp = read_moves("input.txt")
        self.assertEqual(task1(inp, "abcdefghijklmnop"), "bijankplfgmeodhc")

    def test_task2(self):
        inp = read_moves("input.txt")
        self.assertEqual(task2(inp, "abcdefghijklmnop", 1), "bijankplfgmeodhc")

    # def test_task2_2(self):
    #     inp = read_moves("input.txt")
    #     self.assertEqual(task2(inp, "abcdefghijklmnop", 1000000000), "aaaaaaaaaaaaa")


if __name__ == '__main__':
    unittest.main()
