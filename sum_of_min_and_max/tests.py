import unittest
import solution

class SumOfMinAndMaxTests(unittest.TestCase):
    def test_sum_array(self):
        self.assertEqual(10,solution.sum_of_min_and_max([1,2,3,4,5,6,8,9]))
    def test_sum_with_negative(self):
        self.assertEqual(90,solution.sum_of_min_and_max([-10,5,10,100]))
    def test_sum_one(self):
        self.assertEqual(2,solution.sum_of_min_and_max([1]))

if __name__ == '__main__':
    unittest.main()
