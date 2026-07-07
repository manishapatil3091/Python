import threading

def ChkPrime(num):

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def DisplayPrime(num_list):

    print("Prime Numbers:")

    for i in num_list:
        if ChkPrime(i):
            print(i, end=" ")
    print()

def DisplayNonPrime(num_list):

    print("Non Prime Numbers:")

    for i in num_list:
        if not ChkPrime(i):
            print(i, end=" ")
    print()

def main():

    num_list = []

    no = int(input("Enter count of numbers in List: "))

    for i in range(no):
        num = int(input("Enter number: "))
        num_list.append(num)

    Prime = threading.Thread(target=DisplayPrime,args=(num_list,))

    NonPrime = threading.Thread(target=DisplayNonPrime,args=(num_list,))
   
    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()

    print("Exit from Main Thread")

if __name__ == "__main__":
    main()