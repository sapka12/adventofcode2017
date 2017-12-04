import unittest
from program import are_anagrams, task1, task2

class TestMethods(unittest.TestCase):

    def test_is_are_anagrams(self):
        self.assertTrue(are_anagrams("asdf", "sdfa"))
        self.assertTrue(are_anagrams("asdf", "asdf"))
        self.assertFalse(are_anagrams("asdf1", "asdf2"))

    def test_task1(self):
        self.assertEquals(task1(), 386)

    def test_task2(self):
        self.assertEquals(task2(), 208)


if __name__ == '__main__':
    unittest.main()
