def Add(num1 , num2):
    
    Ans = num1 + num2
    return Ans

def main():

    no1 = int(input("Enter 1st a number : "))
    no2 = int(input("Enter 2nd a number : "))
    result = Add(no1,no2)

    print("Addition is : ",result)

if(__name__ == "__main__"):
    main()
