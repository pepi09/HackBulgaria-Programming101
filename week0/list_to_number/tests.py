import unittest
import solution

class ListToNumberTests(unittest.TestCase):
    def test_different_digits(self):
        self.assertEqual(123,solution.list_to_number([1,2,3]))
    def test_same_digits(self):
        self.assertEqual(99999,solution.list_to_number([9, 9, 9, 9, 9]))
    
if __name__ == '__main__':
    unittest.main()
