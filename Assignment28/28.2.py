import sys

def WordsCount(FileName):

    try:
        count = 0 
        with open(FileName, "r") as file:
            for line in file:
                words = line.split()      # Split line into words
                count = count + len(words)
        
        #FileName.close()
        return count

    except FileNotFoundError as fobj:
        print("File is not present in currect directory")

def main():

    if (len(sys.argv) == 2):
        Ret = WordsCount(sys.argv[1])
        print(f"Total number of Words in File : {(sys.argv[1])}  is : {Ret}")
    else:
        print("Invalid number of arguments , please provide file name.")

if __name__ == "__main__":
    main()
