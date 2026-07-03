#  Write a progarm which accepts one number and prints its factors

def Factor_num(num1):

    factr=[]

    for i in range(1, num1+1):

        if num1 % i == 0:

            factr.append(i)

    return factr

def main():

    no = int(input("Enter a Number : "))
    
    ret = Factor_num(no)

    print("Factors for this number are : ", ret )
   
if(__name__ == "__main__"):
    main()

