import unittest
import solution

class IsPrimeTests(unittest.TestCase):
    def test_one(self):
        self.assertFalse(solution.is_prime(1))
    def test_prime(self):
        self.assertTrue(solution.is_prime(3))
    def test_not_prime(self):
        self.assertFalse(solution.is_prime(9))
    def test_negative(self):
        self.assertFalse(solution.is_prime(-10))

if __name__ == '__main__':
    unittest.main()