import unittest
import solution
from subprocess import call
import os

class ConcatFilesTest(unittest.TestCase):
    def setUp(self):
        self.file1 = open("file1","w")
        self.f1 = self.file1.write("aaa")
        self.file2 = open("file2","w")
        self.f2 = self.file2.write("bbb")
        self.file3 = open("MEGATRON","w")
        self.f3 = self.file3.write("ccc")
        self.file3.close()
    def test_concat_files(self):
        self.n1 = len(self.file1.read())
        self.n2 = len(self.file2.read())
        self.n3 = len(self.file3.read())
        call("python3.3 solution.py file1.txt file2.txt",shell = True)
        f = open("MEGATRON","r")
        self.n4 = len(f.read())
        self.assertEqual(self.n1+self.n2+self.n3,n4)
    def tearDown(self):
        os.remove("file1")
        os.remove("file2")
        os.remove("MEGATRON")

if __name__ == '__main__':
    unittest.main()



