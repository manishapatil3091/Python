# Write a lamba function which accepts one number and returns square of that number

ChkSquare = lambda num1 : num1*num1

def main():

    no1 = int(input("Enter Number : "))
    
    SQ = ChkSquare(no1)  

    print("Square is : ",SQ)  
    
if(__name__ == "__main__"):
    main()