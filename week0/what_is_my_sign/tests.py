import unittest
import solution

class WhatIsMySignTests(unittest.TestCase):
    def test_Leo(self):
        self.assertEqual("Leo",solution.what_is_my_sign(5,8))
    def test_Gemini(self):
        self.assertEqual("Gemini",solution.what_is_my_sign(13,6))
    def test_Virgo(self):
        self.assertEqual("Virgo",solution.what_is_my_sign(9,9))
    
if __name__ == '__main__':
    unittest.main()