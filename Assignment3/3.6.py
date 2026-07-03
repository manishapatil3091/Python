# What is difference between print() and return , explain with function example

import sys  #for using getsizeof

def RetFunc(value):

    ret1=type(value)
    ret2= id(value)
    ret3=sys.getsizeof(value)

    return ret1 , ret2 , ret3


def main():

    Value =input("Enter value : ")

    Ret1 , Ret2 , Ret3 = RetFunc(Value)

    print("Date type of Value is : ",Ret1) 
    print("Memory Address of Value is : ",Ret2)  
    print("Size in Bytes of Value is : ",Ret3)   

if(__name__ == "__main__"):
    main()