import unittest
import solution

class IsIncreasingTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution.is_increasing([1,2,3,4,5]))
    def test_true_one_digit_number(self):
        self.assertTrue(solution.is_increasing([1]))
    def test_false(self):
        self.assertFalse(solution.is_increasing([5,6,-10]))
    def test_false_same_digits(self):
        self.assertFalse(solution.is_increasing([1,1,1,1]))
    
if __name__ == '__main__':
    unittest.main()