import unittest
from program import task1, task2


class TestMethods(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(task1("example.txt"), "tknk")
        self.assertEqual(task1("input.txt"), "rqwgj")

    def test_task2(self):
        self.assertEqual(task2("example.txt"), 60)
        self.assertEqual(task2("input.txt"), 333)


if __name__ == '__main__':
    unittest.main()
