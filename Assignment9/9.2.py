# Write a progarm which contains one function named ChkGreater() that accepts two numbers and prints the greater number

def ChkGreater(num1 , num2):

    if(num1>num2):

        print("Greater number is : ",num1)

    else:

        print("Greater number is : ",num2)

def main():

    no1 = int(input("Enter 1st number : "))
    no2 = int(input("Enter 2nd number : "))

    ChkGreater(no1,no2)    
    
if(__name__ == "__main__"):
    main()
