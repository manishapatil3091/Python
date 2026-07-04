# Write a lambda function using map() which accepts list of number and returns list of squares of each number

SquareMap = lambda num_list: list(map(lambda num : num * num , num_list)) 
#SquareMap = list(map(lambda num : num * num, num_list))

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter number: "))
        num_list.append(num)

    SQ = SquareMap(num_list)  

    print("List of Numbers is : ",num_list) 
    print("List of Squares is : ",SQ)  
    
if(__name__ == "__main__"):
    main()