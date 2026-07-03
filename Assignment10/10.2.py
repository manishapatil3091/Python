# Write a progarm which accepts one number and prints sum of fist N numbers

def Nsum(num1):

    sum=0

    for i in range(1,num1+1):

        sum= sum+ i

    print("Sum of N numbers is : ",sum)

def main():

    no1 = int(input("Enter Number : "))
    
    Nsum(no1)    
    
if(__name__ == "__main__"):
    main()
