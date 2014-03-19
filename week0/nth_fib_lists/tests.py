import solution
import unittest

class NthFibListsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1],solution.nth_fib_lists([1], [2], 1))
    def test_2(self):
        self.assertEqual([2],solution.nth_fib_lists([1], [2], 2))
    def test_3(self):
        self.assertEqual([1, 2, 1, 3],solution.nth_fib_lists([1, 2], [1, 3], 3))
    def test_4(self):
        self.assertEqual([1, 2, 3, 1, 2, 3],solution.nth_fib_lists([], [1, 2, 3], 4))
    def test_5(self):
        self.assertEqual([],solution.nth_fib_lists([], [], 100))
    

if __name__ == '__main__':
    unittest.main()