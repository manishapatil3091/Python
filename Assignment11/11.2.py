# Write a progarm which accepts one number and prints number of digit in that number
def Digit_num(num1):

    print("The the number of Digits in this number is : ", len(num1))

def main():

    no1 = input("Enter Number : ")
    
    Digit_num(no1)
   
if(__name__ == "__main__"):
    main()
