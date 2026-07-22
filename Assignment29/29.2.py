import os
import sys

def main():

    if (len(sys.argv) == 2):
        ret = os.path.exists(sys.argv[1])
    
    if ret == True:
        
        fobj = open(sys.argv[1],"r")
        Data = fobj.read()  
        print("Data from file : ",Data)
    else:
        print("There is No such a file in currect directory")
  
if __name__ == "__main__":
    main()