import sys
def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file = open(filename,"r")
        numbers = file.read()
        print(numbers)
        num = numbers.split()
        sum = 0
        for i in range(0,len(num)):
            sum += int(num[i])
        print(sum)
    else:
        print("No agruments given!")
    file.close()

if __name__ == '__main__':
    main()