
def display_star(num):

    for i in range(num):

        for j in range(num):

            print(' * ' , end =" ")

        print()
        
def main():

    no = int(input("Enter a number : "))
    display_star(no)

if(__name__ == "__main__"):
    main()
