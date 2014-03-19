import sys

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        file = open(filename,"r")
        print(file.read())
        print(sys.argv)
        file.close()
    else:
        print("No arguments given!")

if __name__ == '__main__':
    main()