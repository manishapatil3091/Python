import sys

def CopyContent(FileName1 , FileName2):

    try:
        with open(FileName1, "r") as fname1:
            data = fname1.read()

        with open(FileName2, "w") as fname2:
            fname2.write(data)
                        
    except FileNotFoundError as fobj:
        print("File is not present in currect directory")

def main():

    if (len(sys.argv) == 3):
        print(f"Data copied from File : {(sys.argv[1])}  to file  : {(sys.argv[2])} successfully ")
        CopyContent(sys.argv[1],(sys.argv[2]))
    else:
        print("Invalid number of arguments , please provide file names.")

if __name__ == "__main__":
    main()
