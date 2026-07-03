# Write a lamba function which accepts two numbers and returns Multiplication

Mult = lambda num1 , num2 : num1 * num2

def main():

    no1 = int(input("Enter First Number : "))
    no2 = int(input("Enter Second Number : "))
    
    Ret = Mult(no1,no2)  

    print("Multiplication is : ", Ret) 

if(__name__ == "__main__"):
    main()