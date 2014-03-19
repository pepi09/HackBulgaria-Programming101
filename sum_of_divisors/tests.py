import unittest
import solution

class SumOfDivisorsTests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(15,solution.sum_of_divisors(8))
    def test_two(self):
        self.assertEqual(8,solution.sum_of_divisors(7))
    def test_three(self):
        self.assertEqual(1,solution.sum_of_divisors(1))
    def test_four(self):
        self.assertEqual(2340,solution.sum_of_divisors(1000))

if __name__ == '__main__':
    unittest.main()

