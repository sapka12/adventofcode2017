import unittest
from program import task1, task2


class TestMethods(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(task1("test.txt"), "ABCDEF")
        # self.assertEqual(task1("input.txt"), "")

    # def test_task2(self):
    #     self.assertEqual(task2("test.txt"), 0)


if __name__ == '__main__':
    unittest.main()