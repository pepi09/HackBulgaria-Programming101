import unittest
import solution

class CountConsonantsTests(unittest.TestCase):
    def test_contains_consonsnts(self):
        self.assertEqual(11,solution.count_consonants("Theistareykjarbunga"))
    def test_no_consonsnts(self):
        self.assertEqual(0,solution.count_consonants("yeeee"))
    
if __name__ == '__main__':
    unittest.main()
