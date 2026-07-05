
def ChkNum(num):

    if num == 0:
        print("Its Zero")
    elif num > 0:
        print("Its Positive")
    else:
        print("Its Negative")
    
def main():
    no = int(input("Enter a number : "))
    ChkNum(no)

if(__name__ == "__main__"):
    main()