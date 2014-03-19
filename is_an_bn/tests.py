import unittest
import solution

class IsAnBnTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution.is_an_bn("aaabbb"))
    def test_false(self):
        self.assertFalse(solution.is_an_bn("pepi"))
    def test_true_empty(self):
        self.assertTrue(solution.is_an_bn(""))
   
if __name__ == '__main__':
    unittest.main()