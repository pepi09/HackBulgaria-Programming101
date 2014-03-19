import os 
import unittest 
from subprocess import call
import solution

class CatTest(unittest.TestCase): 
    def setUp(self): 
        self.file_name = "test" 
        self.file_handle = open(self.file_name, "w") 
    def test_cat(self): 
        self.file_handle.write("    sdfg") 
        self.file_handle.close() 
        call("python3.3 solution.py " + self.file_name, shell=True) 
        f = open(self.file_name, "r") 
        contents = f.read() 
        f.close()
        self.assertEqual("    sdfg",contents) 
    def tearDown(self): 
        os.remove(self.file_name)

if __name__ == '__main__':
    unittest.main()