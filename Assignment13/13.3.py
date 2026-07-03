# Write a progarm which accepts one number and checks whether it is perfect or not

def Perfect_num(num1):

    sum=0

    for i in range(1,num1):

        if(num1 % i)==0:

            sum=sum+i
    
    if  sum == num1:

        return True

def main():

    no = int(input("Enter a Number : "))
    
    Ret = Perfect_num(no)

    if Ret == True:

        print("This is Perfect Numner")

    else:

        print("This is not a perfect number")
   
if(__name__ == "__main__"):
    main()
