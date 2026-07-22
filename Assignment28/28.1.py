import sys

def LineCount(FileName):

    try:
        count = 0 
        with open(FileName, "r") as file:
            for line in file:
                count = count + 1
        
        #FileName.close()
        return count

    except FileNotFoundError as fobj:
        print("File is not present in currect directory")

def main():

    if (len(sys.argv) == 2):
        Ret = LineCount(sys.argv[1])
        print(f"Total Number of Lines in File : {(sys.argv[1])}  is : {Ret}")
    else:
        print("Invalid number of arguments , please provide file name.")

if __name__ == "__main__":
    main()
