# What is difference between Funtion with parameter and without parameter ?
# Give one example of each 
#-------------------------------------------------------------------------
# A parameter is a variable written in function definition
# A funtion with parameter requires one or more input from user to perofrm the task 
# A funtion without parameter does not require any input from user to perform the task


# Funtion with Parameter
def Mult(no1,no2):

    Ans =no1*no2 
    return Ans


# Function without Parameter
def Display():

    print("You are in Function without parameter")

def main():

    Value1 =int(input("Enter 1st Nmber: "))

    Value2 =int(input("Enter 2nd Nmber: "))

    Ret= Mult(Value1,Value2)

    print("Multiplication is : ",Ret)

    Display()
    
    
if(__name__ == "__main__"):
    main()


