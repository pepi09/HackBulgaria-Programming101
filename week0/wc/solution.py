import sys
def main():
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        file = open(filename,"r")
        count = 0

        if sys.argv[1] == "chars":
            chars = file.read()
            for i in range(0,len(chars)):
                count+=1

        if sys.argv[1] == "words":
            words = file.read().split()
            for i in range(0,len(words)):
                count += 1
        
        if sys.argv[1] == "lines":
            lines = file.read().split("\n")
            for i in range(0,len(lines)):
                count += 1
        file.close()
        return count
    else:
        print("No agruments given!")

if __name__ == '__main__':
    main()