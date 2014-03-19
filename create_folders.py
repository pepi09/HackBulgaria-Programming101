from subprocess import call
import os

def create_folders():
    ss = open("jjj","w")
    filename = open("functions.txt","r")
    text = filename.read()
    text = text.split('\n')
    for line in text:
       # rez = call("mkdir %s" %(line),shell = True)
        os.chdir("/home/pepas/HackBulgaria-Programming101/%s" %(line))
        print("%s" %line)
        solution = open("solution.py","w")
        solution.write("%s" %(line))
        test = open("tests.py","w")
        test.write("%s" %(line))

def main():
    create_folders()

if __name__ == '__main__':
    main()
