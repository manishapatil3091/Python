
def ChkDiv5(num):

    if num % 5 == 0:
        return True
    else:
        return False
    
def main():
    no = int(input("Enter a number : "))
    ret=ChkDiv5(no)

    if ret == True:
        print("Divisible by 5")
    else:
        print("No divisible by 5")

if(__name__ == "__main__"):
    main()