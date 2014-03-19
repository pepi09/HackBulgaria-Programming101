import unittest
import solution
from subprocess import call
import os

class ConcatFilesTest(unittest.TestCase):
    def setUp(self):
        self.file1 = open("file1.txt","w")
        self.f1 = self.file1.write("aaa")
        self.file2 = open("file2.txt","w")
        self.f2 = self.file2.write("bbb")
        self.file3 = open("MEGATRON","w")
        self.f3 = self.file3.write("ccc")
        self.file3.close()
        self.file2.close()
        self.file1.close()
    def test_concat_files(self):
        self.f = open("file1.txt","r")
        self.ff = open("file2.txt","r")
        self.fff = open("MEGATRON","r")
        self.n1 = len(self.f.read())
        self.n2 = len(self.ff.read())
        self.n3 = len(self.fff.read())
        call("python3.3 solution.py file1.txt file2.txt",shell = True)
        self.fi = open("MEGATRON","r")
        n4 = len(self.fi.read())
        self.assertEqual(self.n1+self.n2+self.n3,n4)
    def tearDown(self):
        os.remove("file1.txt")
        os.remove("file2.txt")
        os.remove("MEGATRON")

if __name__ == '__main__':
    unittest.main()



