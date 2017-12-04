import unittest
from program import is_valid, are_anagrams

class TestMethods(unittest.TestCase):

    def test_is_valid(self):
        self.assertTrue(is_valid("aa bb cc dd ee"))
        self.assertFalse(is_valid("aa bb cc dd aa"))
        self.assertTrue(is_valid("aa bb cc dd aaa"))


    def test_is_are_anagrams(self):
        self.assertTrue(are_anagrams("asdf", "sdfa"))
        self.assertTrue(are_anagrams("asdf", "asdf"))
        self.assertFalse(are_anagrams("asdf1", "asdf2"))


if __name__ == '__main__':
    unittest.main()
