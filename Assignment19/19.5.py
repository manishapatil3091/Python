from functools import reduce

ChkPrime = lambda No: No > 1 and all(No % i != 0 for i in range(2, No))

ChkMult = lambda No : No * 2

ChkAdd = lambda no1, no2 : no1 if no1 > no2 else no2


def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter numbers: "))
        num_list.append(num)

    FData = list(filter(ChkPrime,num_list)) 
    print("List after filter: ",FData)

    MData = list(map(ChkMult,FData))    
    print("List after Map: ",MData)

    RData = reduce(ChkAdd,MData)
    print("Output of Reduce: ",RData)

  

if __name__ == "__main__":
    main()