# Write a lambda function using reduce() which accepts list of number and returns product of all elements in it

from functools import reduce

ChkProduct = lambda num_list : reduce(lambda sum , num : sum * num ,num_list)

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter number: "))
        num_list.append(num)

    prd = ChkProduct(num_list)  

    print("List of Numbers is : ",num_list) 
    print("Product of all elements in list is : ",prd)  
    
if(__name__ == "__main__"):
    main()