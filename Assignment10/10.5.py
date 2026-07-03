# Write a progarm which accepts one number and prints all Odd numbers till that number
def Odd_num(num1):

    En = []
    for i in range(1,num1+1):

        if (i%2 != 0):
            
            En.append(i)

    print("Even numbers till this number : ",En)

def main():

    no1 = int(input("Enter Number : "))
    
    Odd_num(no1)    
    
if(__name__ == "__main__"):
    main()
