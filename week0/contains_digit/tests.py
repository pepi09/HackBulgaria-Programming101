import unittest
import solution

class ContainsDigitTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution.contains_digit(123,3))
    def test_false(self):
        self.assertFalse(solution.contains_digit(42,3))

if __name__ == '__main__':
    unittest.main()