import unittest
from program import task1


class TestMethods(unittest.TestCase):
    def test_task1(self):
        self.assertEqual(task1("test.txt"), ("ABCDEF", 38))
        self.assertEqual(task1("input.txt"), ("VEBTPXCHLI", 18702))


if __name__ == '__main__':
    unittest.main()