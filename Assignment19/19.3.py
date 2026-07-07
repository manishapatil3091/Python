from functools import reduce

FCheck = lambda No: No >= 70 and No <= 90

Increment = lambda No : No + 10

Prod = lambda no1, no2: no1 * no2


def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter numbers: "))
        num_list.append(num)

    FData = list(filter(FCheck,num_list)) 
    print("List after filter: ",FData)

    MData = list(map(Increment,FData))    
    print("List after Map: ",MData)

    RData = reduce(Prod,MData)
    print("Output of Reduce: ",RData)

  

if __name__ == "__main__":
    main()