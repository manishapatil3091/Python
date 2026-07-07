
import threading

def EvenFactorCal(num):

    EvenSum = 0 
    for i in range(1, num + 1):

        if num % i == 0 and i % 2 == 0:  # Factor and even logic
            EvenSum = EvenSum + i
           
    print("Summation of Even Factors : ",EvenSum)

def OddFactorCal(num):

    OddSum = 0 
    for i in range(1, num + 1):

        if num % i == 0 and i % 2 != 0: # Factor and Odd logic
            OddSum = OddSum + i

    print("Summation of Odd Factors : ",OddSum)

def main():

    no = int(input("Enter a Number: "))

    EvenFactor = threading.Thread(target=EvenFactorCal , args=(no,))
    OddFactor = threading.Thread(target=OddFactorCal , args=(no,))

    EvenFactor.start()
    OddFactor.start()
    EvenFactor.join()
    OddFactor.join()

    print("Exit from Main Thread")

if __name__ == "__main__" :
    main()
