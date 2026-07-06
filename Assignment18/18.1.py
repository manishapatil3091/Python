
def Add_Elements(num_list1):

    Sum = 0
    for i in num_list1:

        Sum = Sum + i

    return Sum

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter numbers: "))
        num_list.append(num)

    ret = Add_Elements(num_list)  

    print("List of Numbers is : ",num_list) 
    print("Addition of elements is : ",ret)  
    
if(__name__ == "__main__"):
    main()
