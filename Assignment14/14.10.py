# Write a lamba function which accepts three numbers and returns largest number

LargestFromGiven = lambda num1 , num2 , num3 : num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num3 else num3)

def main():

    no1 = int(input("Enter First Number : "))
    no2 = int(input("Enter Second Number : "))
    no3 = int(input("Enter Third Number : "))
    
    Ret = LargestFromGiven(no1,no2,no3)  

    print("Largest Number is : ", Ret) 

if(__name__ == "__main__"):
    main()