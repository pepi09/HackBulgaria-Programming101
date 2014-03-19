from glob import glob
from subprocess import call

def commit():
    folders = glob("*")
    print (folders)
    for i in folders:
        call("git add %s" %(i),shell = True)
        call("git commit -m 'Add files for %s'" %(i),shell = True)
def main():
    commit()
if __name__ == '__main__':
    main()