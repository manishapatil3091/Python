
import threading

def EvenCal(num):

    EvenSum = 0 
    for i in num:

        if i % 2 == 0:  # Even logic
            EvenSum = EvenSum + i
           
    print("Summation of Even Elements ",EvenSum)

def OddCal(num):

    OddSum = 0 
    for i in num:

        if i % 2 != 0: # Odd logic
            OddSum = OddSum + i

    print("Summation of Odd Elements : ",OddSum)

def main():

    num_list = []

    no = int(input("Enter Count of Numbers for the List : "))

    for i in range(no):

        num = int(input("Enter numbers: "))
        num_list.append(num)

    EvenList = threading.Thread(target=EvenCal , args=(num_list,))
    OddList = threading.Thread(target=OddCal , args=(num_list,))

    EvenList.start()
    OddList.start()
    EvenList.join()
    OddList.join()

    print("Exit from Main Thread")

if __name__ == "__main__" :
    main()
