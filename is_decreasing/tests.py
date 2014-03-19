import unittest
import solution

class IsDecreasingTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution.is_decreasing([5,4,3,2,1]))
    def test_false(self):
        self.assertFalse(solution.is_decreasing([1,2,3]))
    def test_false_same_digits(self):
        self.assertFalse(solution.is_decreasing([1,1,1,1]))
    
if __name__ == '__main__':
    unittest.main()