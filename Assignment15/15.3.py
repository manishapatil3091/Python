# Write a lambda function using filter() which accepts list of number and returns list of odd numbers in it 

ChkOdd = lambda num_list : list(filter(lambda num : num % 2 != 0 ,num_list))

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter number: "))
        num_list.append(num)

    Odd_num = ChkOdd(num_list)  

    print("List of Numbers is : ",num_list) 
    print("List of Odd numbers is : ",Odd_num)  
    
if(__name__ == "__main__"):
    main()