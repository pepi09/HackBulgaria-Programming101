from subprocess import call
import solution
import os 
import unittest 

class GenerateNumbersTest(unittest.TestCase): 
    def setUp(self):
        file = open("test.txt","w")
        call("py solution.py test.txt 10",shell = True)
        file.close()
    def test_generate_numbers(self): 
        filename = open("test.txt","r")
        f = filename.read()
        filename.close()
        f = f.split(" ")
        self.assertEqual(10,len(f))
    def tearDown(self): 
        os.remove("test.txt")

if __name__ == '__main__':
    unittest.main()