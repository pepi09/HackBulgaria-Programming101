import unittest
import solution

class CountSubstringsTests(unittest.TestCase):
    def test_contains_string(self):
        self.assertTrue(solution.count_substrings("This is a test string", "is"))
    def test_does_not_contains_string(self):
        self.assertFalse(solution.count_substrings("We have nothing in common!", "really?"))
    def test_capital_letters(self):
        self.assertTrue(solution.count_substrings("This is this and that is this", "this"))
    
if __name__ == '__main__':
    unittest.main()