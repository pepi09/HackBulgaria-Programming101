import unittest
import solution

class ContainsDigitsTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution.contains_digits(402123,[0,3,4]))
    def test_false(self):
        self.assertFalse(solution.contains_digits(666,[6,4]))

if __name__ == '__main__':
    unittest.main()