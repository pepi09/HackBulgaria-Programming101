import unittest
import solution

class CountVowelsTests(unittest.TestCase):
    def test_contains_vowels(self):
        self.assertEqual(8,solution.count_vowels("Theistareykjarbunga"))
    def test_no_vowels(self):
        self.assertEqual(0,solution.count_vowels("grrrrgh!"))
    
if __name__ == '__main__':
    unittest.main()
