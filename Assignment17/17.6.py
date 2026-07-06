
def display_star(num):

    for i in range(num,0,-1):

        for j in range(i):

            print(' * ' , end =" ")

        print()
        
def main():

    no = int(input("Enter a number : "))
    display_star(no)

if(__name__ == "__main__"):
    main()
