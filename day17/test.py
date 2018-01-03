import unittest
from program import task1, task2


class TestMethods(unittest.TestCase):

    def test_task1(self):
        self.assertEqual(task1(3, 2017), 638)
        self.assertEqual(task1(328, 2017), 1670)

    def test_task2(self):
        self.assertEqual(task2(328, 50000000), 2316253)


if __name__ == '__main__':
    unittest.main()
