import unittest
from day3 import maximum, generate_square

class TestMethods(unittest.TestCase):

    def test_max(self):
        self.assertEqual(maximum([[1]]), 1)
        self.assertEqual(maximum([[1, 2]]), 2)
        self.assertEqual(maximum([[1, 2], [3]]), 3)
        self.assertEqual(maximum([[1, 4, 2], [3]]), 4)
        
    def test_generate_square(self):
		self.assertEqual(generate_square(0), [[1]])
		self.assertEqual(generate_square(1), 
		[
			[5, 4, 3],
			[6, 1, 2],
			[7, 8, 9]
		]
		)
		self.assertEqual(generate_square(2), 
		[
			[17, 16, 15, 14, 13],
			[18,  5,  4,  3, 12],
			[19,  6,  1,  2, 11],
			[20,  7,  8,  9, 10],
			[21, 22, 23, 24, 25]
		]
		)


if __name__ == '__main__':
    unittest.main()
