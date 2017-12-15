import unittest
from program import task1, task2, hexa_to_binary, find_neighbours


class TestMethods(unittest.TestCase):
    def test_find_neighbours(self):
        self.assertEqual(find_neighbours([
            [1]
        ]), {(0, 0): []})
        self.assertEqual(find_neighbours([
            [0]
        ]), {})
        self.assertEqual(find_neighbours([
            [0, 1],
            [1, 0]
        ]), {
            (0, 1): [],
            (1, 0): []
        })
        self.assertEqual(find_neighbours([
            [0, 1],
            [1, 1]
        ]), {
            (0, 1): [(1, 1)],
            (1, 0): [(1, 1)],
            (1, 1): [(1, 0), (0, 1)],
        })

    def test_hexa_to_binary(self):
        self.assertEqual(hexa_to_binary("00"), "00000000")
        self.assertEqual(hexa_to_binary("0"), "0000")
        self.assertEqual(hexa_to_binary("1"), "0001")
        self.assertEqual(hexa_to_binary("2"), "0010")
        self.assertEqual(hexa_to_binary("3"), "0011")
        self.assertEqual(hexa_to_binary("4"), "0100")
        self.assertEqual(hexa_to_binary("5"), "0101")
        self.assertEqual(hexa_to_binary("6"), "0110")
        self.assertEqual(hexa_to_binary("7"), "0111")
        self.assertEqual(hexa_to_binary("8"), "1000")
        self.assertEqual(hexa_to_binary("9"), "1001")
        self.assertEqual(hexa_to_binary("a"), "1010")
        self.assertEqual(hexa_to_binary("b"), "1011")
        self.assertEqual(hexa_to_binary("c"), "1100")
        self.assertEqual(hexa_to_binary("d"), "1101")
        self.assertEqual(hexa_to_binary("e"), "1110")
        self.assertEqual(hexa_to_binary("f"), "1111")
        self.assertEqual(hexa_to_binary("a0c2"), "1010000011000010")

    def test_task1(self):
        self.assertEqual(task1("flqrgnkx"), 8108)
        self.assertEqual(task1("ljoxqyyw"), 8316)

    def test_task2(self):
        self.assertEqual(task2("flqrgnkx"), 1242)
        self.assertEqual(task2("ljoxqyyw"), 1074)


if __name__ == '__main__':
    unittest.main()
