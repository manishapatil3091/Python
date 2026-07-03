# Write a progarm which accepts one number and checks if it is palindrome or not

def Palindrome_num(num1):

    reverse = ""

    for i in num1:
        
        reverse = i + reverse # here we are doing i plus reserve and not reverse plus so it will append string in reverse

    if reverse == num1:

        print("This is Palindrome number" )

    else:

        print("This number is Not Palindrome number" )

def main():

    no1 = input("Enter Number : ")  # input is taken as string
    
    Palindrome_num(no1)
   
if(__name__ == "__main__"):
    main()

