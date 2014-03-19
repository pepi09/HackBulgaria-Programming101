import unittest
import solution

class NthFibonacciTests(unittest.TestCase):
    def test_first(self):
        self.assertEqual(1,solution.nth_fibonacci(1))
    def test_second(self):
        self.assertEqual(1,solution.nth_fibonacci(2))
    def test_third(self):
        self.assertEqual(2,solution.nth_fibonacci(3))
    def test_tenth(self):
        self.assertEqual(55,solution.nth_fibonacci(10))

if __name__ == '__main__':
    unittest.main()