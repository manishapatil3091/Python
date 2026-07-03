# Write a lamba function which accepts one number and returns True if it is Even else False

ChkEvenOdd = lambda num1 : num1 % 2 == 0

def main():

    no1 = int(input("Enter a Number : "))
    
    Ret = ChkEvenOdd(no1)  

    if Ret == True:
        print("It is an Even Number")  

    else:
        print("It is an Odd Number") 

if(__name__ == "__main__"):
    main()