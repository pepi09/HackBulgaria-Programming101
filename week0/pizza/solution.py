import sys

def main():
    Customers = {}
    while True:
        command = input("Enter command>")
        command = command.split()
        if command[0] == "take":
            if command[1] in Customers:
                Customers["%s" %(command[1])] += command[2]
            else:
                Customers["%s" %(command[1])] = command[2]
            print ("Taking order from %s for %s." %(command[1],command[2]))
        if command[0] == "status":
            print(Customers)
            for key in Customers:
                print("%s - %s" % (key,Customers[key]))

        if command[0] == "finish":
            break

if __name__ == '__main__':
    main()