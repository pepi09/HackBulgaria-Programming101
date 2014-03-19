from subprocess import call
import solution
import os 
import unittest 

class GenerateNumbersTest(unittest.TestCase): 
    def setUp(self):
        call("python3.3 solution.py test.txt 10")
    def test_generate_numbers(self): 
        filename = open("test""r")
        f = filename.read()
        self.assertEqual(10,len(f))
    def tearDown(self): 
        os.remove("test")

if __name__ == '__main__':
    unittest.main()