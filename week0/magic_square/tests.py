import unittest
from solution import magic_square

class MagicSquare(unittest.TestCase):
    def test_true(self):
        self.assertTrue(magic_square([[4,9,2], [3,5,7], [8,1,6]]))
    def test_false(self):
        self.assertFalse(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
if __name__ == '__main__':
    unittest.main()