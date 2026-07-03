# Write a progarm which accepts one number and prints multiplication table for that number

def MultTable(num1):

    for i in range(1,11):

        print(num1*i)    

def main():

    no1 = int(input("Enter Number : "))
    
    MultTable(no1)    
    
if(__name__ == "__main__"):
    main()
