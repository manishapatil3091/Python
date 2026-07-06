
def Search_Element(num_list1,num1):

    EleCount =  0
    for i in num_list1:

        if i == num1:
            EleCount = EleCount+1
            
    return EleCount

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter numbers: "))
        num_list.append(num)

    Search_num = int(input("Enter Element to Search in list : "))

    ret = Search_Element(num_list,Search_num)  

    print("List of Numbers is : ",num_list) 
    print(f"Count of {Search_num} in list is: {ret}")  
    
if(__name__ == "__main__"):
    main()
