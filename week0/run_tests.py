from glob import glob
from subprocess import call
import os

def run_tests():
    folders = glob("*")
    for i in folders:
        os.chdir("/home/pepas/HackBulgaria-Programming101/week0/%s" %(i))
        call("py tests.py",shell = True)

def main():
    run_tests()

if __name__ == '__main__':
    main()