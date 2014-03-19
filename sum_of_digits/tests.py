import unittest
import solution

class SumOfDigitsTests(unittest.TestCase):
    def test_first(self):
        self.assertEqual(43,solution.sum_of_digits(1325132435356))
    def test_second(self):
        self.assertEqual(6,solution.sum_of_digits(123))
    def test_one_digit(self):
        self.assertEqual(6,solution.sum_of_digits(6))
    def test_negative(self):
        self.assertEqual(1,solution.sum_of_digits(-10))

if __name__ == '__main__':
    unittest.main()
