# Write a lambda function using reduce() which accepts list of number and returns Minimum element from it

from functools import reduce

ChkMinimum = lambda num_list : reduce(lambda a , b : a if a < b else b ,num_list)

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter number: "))
        num_list.append(num)

    minm = ChkMinimum(num_list)  

    print("List of Numbers is : ",num_list) 
    print("Maximum element from the list is : ",minm)  
    
if(__name__ == "__main__"):
    main()