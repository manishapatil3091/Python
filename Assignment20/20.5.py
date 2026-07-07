
import threading

def EvenNum(num):

    for i in range(1, num + 1):

        print(i, end=" ")
    
    print()

def OddNum(num):

    for i in range(num ,0,-1):

        print(i, end=" ")

    print()

def main():

    Thred1 = threading.Thread(target=EvenNum , args=(50,))
    Thred2 = threading.Thread(target=OddNum , args=(50,))

    Thred1.start()
    Thred2.start()
    Thred1.join()
    Thred2.join()

    print("Exit from Main Thread")

if __name__ == "__main__" :
    main()
