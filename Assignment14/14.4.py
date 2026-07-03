# Write a lamba function which accepts two numbers and returns Minimum number

ChkMin = lambda num1 ,num2 : num1 if num1m< num2 else num2

def main():

    no1 = int(input("Enter First Number : "))
    no2 = int(input("Enter Second Number : "))
    
    Ret = ChkMin(no1,no2)  

    print("Minimum number is : ",Ret)  

if(__name__ == "__main__"):
    main()