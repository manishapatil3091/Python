import sys

def ReadLine(FileName):

    try:
        with open(FileName, "r") as file:
            for line in file:
                print(line)
                        
    except FileNotFoundError as fobj:
        print("File is not present in currect directory")

def main():

    if (len(sys.argv) == 2):
        print(f"Data from File : {(sys.argv[1])}  is :","\n")
        ReadLine(sys.argv[1])
    else:
        print("Invalid number of arguments , please provide file name.")

if __name__ == "__main__":
    main()
