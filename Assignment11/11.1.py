# Write a progarm which accepts one number and checks whether it is prime or not
def Prime_num(num1):

    if num1 >= 1:

        for i in range (2,num1):

            if(num1 % i) == 0:

                return False

        return True

def main():

    no1 = int(input("Enter Number : "))
    
    ret=Prime_num(no1)

    if ret == True:

        print("It is a Prime Number")

    else:

        print("It is not Prime Number")
    
if(__name__ == "__main__"):
    main()
