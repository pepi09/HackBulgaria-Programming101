import unittest
import solution

class PrimeNumberOfDivisorsTests(unittest.TestCase):
    def test_false(self):
        self.assertFalse(solution.prime_number_of_divisors(8))
    def test_true(self):
        self.assertTrue(solution.prime_number_of_divisors(7))

if __name__ == '__main__':
    unittest.main()
