import os
import sys

def main():

    if (len(sys.argv) == 2):
        ret = os.path.exists(sys.argv[1])
    
    if ret == True:
        print("File is present in currect directory")
    else:
        print("There is No such a file in currect directory")
  
if __name__ == "__main__":
    main()