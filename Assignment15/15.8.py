# Write a lambda function using filter() which accepts list of number and returns numbers which are divisible by 3 and 5 

ChkDiv = lambda num_list :list(filter(lambda num1 : num1 % 5 == 0 and num1 % 3 ==0 ,num_list))

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter number: "))
        num_list.append(num)

    Div = ChkDiv(num_list)  

    print("List of Numbers is : ",num_list) 
    print("Elements from the list which are divisible by 3 and 5 are : ",Div)  
    
if(__name__ == "__main__"):
    main()