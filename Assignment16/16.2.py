def ChkNum(num):
    
    if num % 2 ==0:
        return True
    else:
        return False

    
def main():

    no = int(input("Enter a number : "))
    result = ChkNum(no)

    if result==True:
        print("It is an Even Number")
    else:
        print("It is an Odd Number")

if(__name__ == "__main__"):
    main()