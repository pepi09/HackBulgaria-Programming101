import sys
from random import randint

def main():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        file = open(filename,"w")
        for i in range(1,int(sys.argv[2])):
            number = randint(1, 1000)
            file.write("%s " %(number))
    else:
        print("No arguments given!")
    file.write("\n")
    file.close()

if __name__ == '__main__':
    main()