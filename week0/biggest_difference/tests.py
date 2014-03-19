import unittest
import solution

class BiggestDifferenceTests(unittest.TestCase):
    def test_two_numbers(self):
        self.assertEqual(-1,solution.biggest_difference([1,2]))
    def test_more_numbers(self):
        self.assertEqual(-4,solution.biggest_difference([1,2,3,4,5]))
    def test_negative_numbers(self):
        self.assertEqual(-9,solution.biggest_difference([-10,-9,-1]))
    def test_range(self):
        self.assertEqual(-99,solution.biggest_difference(range(100)))

if __name__ == '__main__':
    unittest.main()