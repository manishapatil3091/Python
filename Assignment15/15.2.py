# Write a lambda function using filter() which accepts list of number and returns list of even numbers in it 

ChkEven = lambda num_list : list(filter(lambda num : num % 2 == 0 ,num_list))

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter number: "))
        num_list.append(num)

    EV_num = ChkEven(num_list)  

    print("List of Numbers is : ",num_list) 
    print("List of Even numbers is : ",EV_num)  
    
if(__name__ == "__main__"):
    main()