# Write a progarm which accepts one number and prints sum of digit in that number

def DigitSum_num(num1):

    sum=0

    for i in num1:

        sum = sum + int(i)

    print("The the Sum of Digits in this number is : ",sum )

def main():

    no1 = list(input("Enter Number : "))
    
    DigitSum_num(no1)
   
if(__name__ == "__main__"):
    main()
