from solution import goldbach
import unittest

class GoldbachTest(unittest.TestCase):
    def test_one_combination(self):
        self.assertEqual([(3,3)],goldbach(6))
    def test_more_coombinations(self):
        self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)],goldbach(100))
   
if __name__ == '__main__':
    unittest.main()