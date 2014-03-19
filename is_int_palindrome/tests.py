import unittest
import solution

class IsIntPalindromeTests(unittest.TestCase):
    def test_true_one_digit(self):
        self.assertTrue(solution.is_int_palindrome(1))
    def test_false(self):
        self.assertFalse(solution.is_int_palindrome(43))
    def test_true_even_digits(self):
        self.assertTrue(solution.is_int_palindrome(100001))
    def test_true_odd_digits(self):
        self.assertTrue(solution.is_int_palindrome(999))

if __name__ == '__main__':
    unittest.main()