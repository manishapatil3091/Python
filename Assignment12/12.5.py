#  Write a progarm which accepts one number and prints that many numbers in reverse order

def num_ser(num):

    for i in range (num , 0 , -1): # num will be deducted by 1 for each iteration , till 1

        print(i)

def main():

    no = int(input("Enter a Number : "))

    num_ser(no)
   
if(__name__ == "__main__"):
    main()