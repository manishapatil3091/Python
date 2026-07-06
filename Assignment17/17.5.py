
def ChkPrime(num):

    if num <= 1 :
        return False

    else :
        for i in range(2,num):

            if(num % i==0):

                return False

        return True


def main():

    no1 = int(input("Enter Number : "))
    
    Ret = ChkPrime(no1)   

    if Ret == True:

        print("It is a prime number")

    else :

        print("It is Not a prime number")
    
if(__name__ == "__main__"):
    main()
