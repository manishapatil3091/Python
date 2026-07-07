
Mult = lambda num1 ,num2: num1 * num2

def main():

    no1 = int(input("Enter first Number : "))
    no2 = int(input("Enter second Number : "))
    
    ret = Mult(no1,no2)  

    print("Multiplication is : ",ret)  
    
if(__name__ == "__main__"):
    main()