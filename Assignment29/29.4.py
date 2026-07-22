import sys

def CompareContent(FileName1 , FileName2):

    try:
        fobj1 = open(FileName1, "r")
        data1 = fobj1.read()

        fobj2 = open(FileName2, "r")
        data2 = fobj2.read()

        if (data1 == data2):
            return True
        else:
            return False
         
    except FileNotFoundError as fobj:
        print("File is not present in currect directory")

def main():

    if (len(sys.argv) == 3):
        Ret = CompareContent((sys.argv[1]),(sys.argv[2]))

        if (Ret == True):
            print("Success")
        else:
            print("Failure")
    else:
        print("Invalid number of arguments , please provide file names.")

if __name__ == "__main__":
    main()
