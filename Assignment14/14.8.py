# Write a lamba function which accepts two numbers and returns addition

Add = lambda num1 , num2 : num1 + num2

def main():

    no1 = int(input("Enter First Number : "))
    no2 = int(input("Enter Second Number : "))
    
    Ret = Add(no1,no2)  

    print("Addition is : ", Ret) 

if(__name__ == "__main__"):
    main()