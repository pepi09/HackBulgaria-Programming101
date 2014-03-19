import solution
import unittest

class MemberOfNthFibListsTests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution.member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
    def test_false(self):
        self.assertFalse(solution.member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))

if __name__ == '__main__':
    unittest.main()
