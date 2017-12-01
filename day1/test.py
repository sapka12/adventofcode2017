import unittest
from captcha import captcha_part_one, captcha_part_two

class TestStringMethods(unittest.TestCase):

    def test_captcha_part_one_1122(self):
        self.assertEqual(captcha_part_one("1122"), 3)

    def test_captcha_part_one_1111(self):
        self.assertEqual(captcha_part_one("1111"), 4)

    def test_captcha_part_one_1234(self):
        self.assertEqual(captcha_part_one("1234"), 0)

    def test_captcha_part_one_91212129(self):
        self.assertEqual(captcha_part_one("91212129"), 9)

    def test_captcha_part_two_1212(self):
        self.assertEqual(captcha_part_two("1212"), 6)

    def test_captcha_part_two_1221(self):
        self.assertEqual(captcha_part_two("1221"), 0)

    def test_captcha_part_two_123425(self):
        self.assertEqual(captcha_part_two("123425"), 4)

    def test_captcha_part_two_123123(self):
        self.assertEqual(captcha_part_two("123123"), 12)


    def test_captcha_part_two_12131415(self):
        self.assertEqual(captcha_part_two("12131415"), 4)


if __name__ == '__main__':
    unittest.main()
