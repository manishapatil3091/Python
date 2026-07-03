# Write a progarm which accepts one number and prints reverse number of that number

def Reverse_num(num1):

    reverse = ""

    for i in num1:
        
        reverse = i + reverse # here we are doing i plus reserve and not reverse plus so it will append string in reverse

    print("The Reverse number is : ",reverse )

def main():

    no1 = input("Enter Number : ")  # input is taken as string
    
    Reverse_num(no1)
   
if(__name__ == "__main__"):
    main()
