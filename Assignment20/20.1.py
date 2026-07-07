import threading

def EvenNum():

    for i in range(2, 21, 2):
        print(i, end=" ")

    print()

def OddNum():

    for i in range(1, 20, 2):
        print(i, end=" ")



def main():

    t1 = threading.Thread(target=EvenNum)
    t2 = threading.Thread(target=OddNum)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__" :
    main()
