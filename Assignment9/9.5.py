# Write a progarm which accepts one number and checks whether it is divisible by 3 and 5

def ChkDiv(num1):

    if(num1%3 ==0 and num1%5 == 0 ):

        print("This number is divisible by 3 and 5")

    else:

        print("This number Not is divisible by 3 and 5")

def main():

    no1 = int(input("Enter Number : "))
    
    ChkDiv(no1)    
    
if(__name__ == "__main__"):
    main()
