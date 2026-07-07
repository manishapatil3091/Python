
ChkPower = lambda num1 : 2**num1

def main():

    no1 = int(input("Enter Number : "))
    
    P = ChkPower(no1)  

    print("Power of 2 is : ",P)  
    
if(__name__ == "__main__"):
    main()