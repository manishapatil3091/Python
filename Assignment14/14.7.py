# Write a lamba function which accepts one number and returns True if divisible by 5

ChkDiv = lambda num1 : num1 % 5 == 0

def main():

    no1 = int(input("Enter a Number : "))
    
    Ret = ChkDiv(no1)  

    if Ret == True:
        print("It is divisible by 5.")  

    else:
        print("It is Not divisible by 5.") 

if(__name__ == "__main__"):
    main()