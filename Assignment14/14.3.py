# Write a lamba function which accepts two numbers and returns maximum number

ChkMax = lambda num1 ,num2 : num1 if num1>num2 else num2

def main():

    no1 = int(input("Enter First Number : "))
    no2 = int(input("Enter Second Number : "))
    
    Ret = ChkMax(no1,no2)  

    print("Maximum number is : ",Ret)  
    
if(__name__ == "__main__"):
    main()