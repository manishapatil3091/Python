# Write a lambda function using filter() which accepts list of strings and returns list of strings having length greater than 5 

ChkStrLen = lambda str_list : list(filter(lambda str3 : len(str3) > 5 ,str_list))

def main():

    str_list = []

    no = int(input("Enter Count of Strings for the List : "))

    for i in range(no):

        str1 = input("Enter string : ")
        str_list.append(str1)

    str2 = ChkStrLen(str_list)  

    print("List of String is : ",str_list) 
    print("Strings having length grater than 5 are : ",str2)  
    
if(__name__ == "__main__"):
    main()