import sys

def main():
    if len(sys.argv) > 1:
        for i in range(1,len(sys.argv)):
            filename = sys.argv[i]
            file = open(filename,"r")
            print(file.read())
            file.close()
    else:
        print("No arguments given!")
    

if __name__ == '__main__':
    main()