import unittest
from program import task1, last_16_bits_match


class TestMethods(unittest.TestCase):
    def test_check_last16(self):
        self.assertTrue(last_16_bits_match(245556042, 1431495498))
        self.assertFalse(last_16_bits_match(1092455, 430625591))
        self.assertFalse(last_16_bits_match(1181022009, 1233683848))
        self.assertFalse(last_16_bits_match(1744312007, 137874439))

    def test_find_neighbours(self):
        self.assertEqual(task1(65, 8921, 5), 1)
        self.assertEqual(task1(65, 8921, 40 * 1000 * 1000), 588)
        self.assertEqual(task1(722, 354, 40 * 1000 * 1000), 612)


if __name__ == '__main__':
    unittest.main()
