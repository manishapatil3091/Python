# Write a lambda function using filter() which accepts list of number and returns Count of even numbers in it 

ChkEvenCount = lambda num_list : len(list(filter(lambda num : num % 2 == 0 ,num_list)))

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter number: "))
        num_list.append(num)

    ev_count = ChkEvenCount(num_list)  

    print("List of Numbers is : ",num_list) 
    print("Count of Even numbers is : ",ev_count)  
    
if(__name__ == "__main__"):
    main()