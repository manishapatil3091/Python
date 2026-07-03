# Write a progarm which accepts one number and prints binary equivalent

def Binary_Equi(num1):

    binary = ""

    while num1 > 0:
        remainder = num1 % 2
        binary = str(remainder) + binary
        num1 = num1 // 2

    return binary

def main():

    no = int(input("Enter a Number : "))
    
    Ret = Binary_Equi(no)

    print("Binary Equivalent is : ",Ret)
   
if(__name__ == "__main__"):
    main()
