#  Write a progarm which accepts one number and prints that many numbers starting from 1.

def num_ser(num):

    for i in range (1,num+1):

        print(i)

def main():

    no = int(input("Enter a Number : "))

    num_ser(no)
   
if(__name__ == "__main__"):
    main()