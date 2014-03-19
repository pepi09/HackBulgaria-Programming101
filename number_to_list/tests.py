import unittest
import solution

class NumberToListTests(unittest.TestCase):
    def test_different_digits(self):
        self.assertEqual([1, 2, 3],solution.number_to_list(123))
    def test_same_digits(self):
        self.assertEqual([9, 9, 9, 9, 9],solution.number_to_list(99999))
    
if __name__ == '__main__':
    unittest.main()
