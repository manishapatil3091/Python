def ChkDiv(num):

    Sum = 0
    for i in range(1,num):

        if(num % i==0):

            Sum=Sum+i

    return Sum

def main():

    no1 = int(input("Enter Number : "))
    
    Ret = ChkDiv(no1)    
    print("Addition of Factorial = ", Ret)
    
if(__name__ == "__main__"):
    main()
