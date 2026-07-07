from functools import reduce

ChkEven = lambda No: No % 2 == 0

ChkSqr = lambda No : No * No

ChkAdd = lambda no1, no2: no1 + no2


def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter numbers: "))
        num_list.append(num)

    FData = list(filter(ChkEven,num_list)) 
    print("List after filter: ",FData)

    MData = list(map(ChkSqr,FData))    
    print("List after Map: ",MData)

    RData = reduce(ChkAdd,MData)
    print("Output of Reduce: ",RData)

  

if __name__ == "__main__":
    main()