
def Facto(num1):

    f =1

    for i in range(1,num1+1):

        f = f*i

    return f

def main():

    no1 = int(input("Enter Number : "))
    
    Ret=Facto(no1)  

    print("Factorial of is : ",Ret)  
    
if(__name__ == "__main__"):
    main()
