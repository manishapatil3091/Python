
def AddDigit(num):

    total = 0

    for i in num:

        total = total + int(i)

    return total

def main():

    no = input("Enter a Number : ")
    result = AddDigit(no)

    print("Length is : ", result)
    
if(__name__ == "__main__"):
    main()