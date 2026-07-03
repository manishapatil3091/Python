# Write a progarm which accepts one number and prints Factorial of that number

def Facto(num1):

    f =1

    for i in range(1,num1+1):

        f = f*i

    print("Factorial of is : ",f)

def main():

    no1 = int(input("Enter Number : "))
    
    Facto(no1)    
    
if(__name__ == "__main__"):
    main()
