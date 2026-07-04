# Write a lambda function using reduce() which accepts list of number and returns addition of all elements in it

from functools import reduce

ChkAddition = lambda num_list : reduce(lambda sum , num : sum + num ,num_list)

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter number: "))
        num_list.append(num)

    sum = ChkAddition(num_list)  

    print("List of Numbers is : ",num_list) 
    print("Addition of all elements in list is : ",sum)  
    
if(__name__ == "__main__"):
    main()