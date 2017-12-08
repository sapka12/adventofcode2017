import unittest
from program import task1, task2


class TestMethods(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(task1("test.txt"), 1)
        self.assertEqual(task1("input.txt"), 6611)

    def test_task2(self):
        self.assertEqual(task2("test.txt"), 10)
        self.assertEqual(task2("input.txt"), 6619)


if __name__ == '__main__':
    unittest.main()
