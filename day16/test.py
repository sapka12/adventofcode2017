import unittest
from program import task1, task2, exchange, spin, partner, do_permutation


def read_moves(input_file):
    with open(input_file) as f:
        return [x.strip() for x in f.readlines()][0].split(",")


def to_arr(str):
    return [str[i] for i in range(len(str))]


def to_str(arr):
    return "".join(arr)


class TestMethods(unittest.TestCase):

    def test_do_permutation(self):
        self.assertEqual(do_permutation(['a', 'b', 'c'], [1, 0, 2]), ['b', 'a', 'c'])

    def test_task1_spin(self):
        self.assertEqual(task1(["s1"], to_arr("abcde")),  to_arr("eabcd"))

    def test_task1_spin2(self):
        self.assertEqual(task1(["s10"], to_arr("abcde")), to_arr("abcde"))

    def test_task1_exchange(self):
        self.assertEqual(task1(["s1", "x3/4"], to_arr("abcde")), to_arr("eabdc"))

    def test_task1_partner(self):
        self.assertEqual(task1(["s1", "x3/4", "pe/b"], to_arr("abcde")), to_arr("baedc"))

    def test_task1(self):
        inp = read_moves("input.txt")
        self.assertEqual(task1(inp, to_arr("abcdefghijklmnop")), to_arr("bijankplfgmeodhc"))

    def test_task2_2rounds(self):
        self.assertEqual(task2(["s1", "x3/4", "pe/b"], to_arr("abcde"), 2), to_arr("ceadb"))

    def test_task2_4rounds(self):
        self.assertEqual(task2(["s1", "x3/4", "pe/b"], to_arr("abcde"), 4), to_arr("abcde"))

    def test_task2_10rounds(self):
        self.assertEqual(to_str(task2(["s1", "x3/4", "pe/b"], to_arr("abcde"), 10)), "ceadb")

    def test_task2_100rounds(self):
        self.assertEqual(to_str(task2(["s1", "x3/4", "pe/b"], to_arr("abcde"), 100)), "abcde")

    def test_task2_102rounds(self):
        self.assertEqual(to_str(task2(["s1", "x3/4", "pe/b"], to_arr("abcde"), 102)), "ceadb")

    def test_task2_2x(self):
        inp = read_moves("input.txt")

        task_twice = task1(inp, task1(inp, to_arr("abcdefghijklmnop")))
        task_x1 = task2(inp, to_arr("abcdefghijklmnop"), 2)

        self.assertEqual(to_str(task_x1), to_str(task_twice))

    # def test_task2_4x(self):
    #     inp = read_moves("input.txt")
    #
    #     task_twice = task1(inp, task1(inp, task1(inp, task1(inp, to_arr("abcdefghijklmnop")))))
    #     task_x1 = task2(inp, to_arr("abcdefghijklmnop"), 4)
    #
    #     self.assertEqual(to_str(task_x1), to_str(task_twice))

    # abcdelghijkfmnop njfimcapbokhelgd bhgcmoinfpkaejdl fadompcbgnkiehlj odnheajcpiklmgbf
    # def test_task2_2(self):
    #     inp = read_moves("input.txt")
    #     self.assertEqual(to_str(task2(inp, to_arr("abcdefghijklmnop"), 1000000000)), "???")


if __name__ == '__main__':
    unittest.main()
