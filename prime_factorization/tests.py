import unittest
import solution

class PrimeFactorizationTests(unittest.TestCase):
    def test_number(self):
        self.assertEqual([(2, 1), (5, 1)],solution.prime_factorization(10))
    def test_prime_number(self):
        self.assertEqual([(89, 1)],solution.prime_factorization(89))
    def test_large_number(self):
        self.assertEqual([(2, 3), (5, 3)],solution.prime_factorization(1000))
    
if __name__ == '__main__':
    unittest.main()