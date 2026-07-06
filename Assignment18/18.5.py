
import MarvellousNum as MN

def ListPrime(num_list1):

    PrimeAdd =  0
    for i in num_list1:

        if MN.ChkPrime(i):
            PrimeAdd = PrimeAdd + i
            
    return PrimeAdd

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter numbers: "))
        num_list.append(num)

    ret = ListPrime(num_list)  

    print("List of Numbers is : ",num_list) 
    print("Addition of Prime Number in list is: ",ret)  
    
if(__name__ == "__main__"):
    main()
