import unittest
import solution

class IsNumberBalancedTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution.is_number_balanced(9))
    def test_false(self):
        self.assertFalse(solution.is_number_balanced(13))
    def test_true_odd_digits(self):
        self.assertTrue(solution.is_number_balanced(121))
    def test_true_even_digits(self):
        self.assertTrue(solution.is_number_balanced(4518))

if __name__ == '__main__':
    unittest.main()