
def Max_Elements(num_list1):

    Maxm =  num_list1[0]
    for i in num_list1:

        if i > Maxm:
            Maxm = i
            
    return Maxm

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter numbers: "))
        num_list.append(num)

    ret = Max_Elements(num_list)  

    print("List of Numbers is : ",num_list) 
    print("Maximum Element is : ",ret)  
    
if(__name__ == "__main__"):
    main()
