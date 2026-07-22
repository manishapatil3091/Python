import sys

def SearchWord(FileName,WordToSearch):

    try:
        count = 0 
        found = False
        with open(FileName, "r") as fobj:
            for line_no, line in enumerate(fobj, start=1):
                if WordToSearch in line:
                    
                    found = True
                    count = count + 1
            return count
            
    except FileNotFoundError as fobj1:
        print("File is not present in currect directory")

def main():

    if (len(sys.argv) == 3):
        Ret = SearchWord(sys.argv[1] , sys.argv[2])
        if (Ret == 0  ):
            print(f"{sys.argv[2]} word is not present in the file.")
        else :
            print(f"{sys.argv[2]} word found in the file {Ret} times .")
    else:
        print("Invalid number of arguments , please provide file name.")

if __name__ == "__main__":
    main()

