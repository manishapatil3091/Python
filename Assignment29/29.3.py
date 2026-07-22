import sys

def CreateCopyContent(FileName):

    try:
        fobj1 = open(FileName, "r")
        data = fobj1.read()

        fobj2 = open("Demo.txt","w")
        fobj2.write(data)
         
    except FileNotFoundError as fobj:
        print("File is not present in currect directory")

def main():

    if (len(sys.argv) == 2):
        print(f" New file Demo.txt created and Data copied from File : {(sys.argv[1])} into it")
        CreateCopyContent(sys.argv[1])
    else:
        print("Invalid number of arguments , please provide file names.")

if __name__ == "__main__":
    main()
