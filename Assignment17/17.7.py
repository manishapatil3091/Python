
def display_pattern_num(num):

    for i in range(1,num+1):

        for j in range(1,num+1):

            print( j , end =" ")

        print()
        
def main():

    no = int(input("Enter a number : "))
    display_pattern_num(no)

if(__name__ == "__main__"):
    main()
