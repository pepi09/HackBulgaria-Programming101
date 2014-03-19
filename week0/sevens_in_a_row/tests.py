import unittest
import solution

class SevensInARowTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution.sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
    def test_false(self):
        self.assertFalse(solution.sevens_in_a_row([1,7,1,7,7], 4))
    def test_true_more_sevens_in_a_row(self):
        self.assertTrue(solution.sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
    def test_true_in_the_beginning(self):
        self.assertTrue(solution.sevens_in_a_row([7,2,1,6,2], 1))

if __name__ == '__main__':
    unittest.main()
