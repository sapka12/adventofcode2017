import unittest
from program import task1, task2, last_16_bits_match, one_round


class TestMethods(unittest.TestCase):

    def test_check_last16(self):
        self.assertTrue(last_16_bits_match(245556042, 1431495498))
        self.assertFalse(last_16_bits_match(1092455, 430625591))
        self.assertFalse(last_16_bits_match(1181022009, 1233683848))
        self.assertFalse(last_16_bits_match(1744312007, 137874439))

    def test_task1(self):
        self.assertEqual(task1(65, 8921, 5), 1)
        self.assertEqual(task1(65, 8921, 40 * 1000 * 1000), 588)
        self.assertEqual(task1(722, 354, 40 * 1000 * 1000), 612)

    def test_gen(self):
        self.assertEqual(one_round(65, 16807, 4), 1352636452)
        self.assertEqual(one_round(8921, 48271, 8), 1233683848)

        self.assertEqual(one_round(1352636452, 16807, 4), 1992081072)
        self.assertEqual(one_round(1233683848, 48271, 8), 862516352)

        self.assertEqual(one_round(1992081072, 16807, 4), 530830436)
        self.assertEqual(one_round(862516352, 48271, 8), 1159784568)

        self.assertEqual(one_round(530830436, 16807, 4), 1980017072)
        self.assertEqual(one_round(1159784568, 48271, 8), 1616057672)

        self.assertEqual(one_round(1980017072, 16807, 4), 740335192)
        self.assertEqual(one_round(1616057672, 48271, 8), 412269392)

    def test_task2(self):
        self.assertEqual(task2(65, 8921, 5), 0)
        self.assertEqual(task2(65, 8921, 5 * 1000 * 1000), 309)
        self.assertEqual(task2(722, 354, 5 * 1000 * 1000), 285)


if __name__ == '__main__':
    unittest.main()
