#what is user-defined funtion ?
#write a program to accept 2 numbers and return iys multiplication
#-------------------------------------------------------------------------
# a function is a named block of code that performs sepcific task.
# and user-defined function is a function which is defined by a programer usning def keyword.

def Mult(no1,no2):

    Ans =no1*no2 
    return Ans


def main():

    Value1 =int(input("Enter 1st Nmber: "))

    Value2 =int(input("Enter 2nd Nmber: "))

    Ret= Mult(Value1,Value2)

    print("Multiplication is : ",Ret)
    
    
if(__name__ == "__main__"):
    main()