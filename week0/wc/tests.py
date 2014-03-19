import unittest
import solution
from subprocess import call

class WCTest(object):
    def setUp(self):
        file = open("test","w")
        file.write("This is\na test!")
    def test_chars(self):
        f = open("test","r")
        self.assertEqual(15,call("py solution.py chars",shell = True))
    def test_words(self):
        f = open("test","r")
        self.assertEqual(4,call("py solution.py words",shell = True))
    def test_lines(self):
        f = open("test","r")
        self.assertEqual(2,call("py solution.py lines",shell = True))
if __name__ == '__main__':
    unittest.main()