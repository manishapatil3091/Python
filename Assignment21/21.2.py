import threading

def Maximum(num_list):

    max_num = num_list[0]

    for i in num_list:

        if i > max_num:
            max_num = i

    print("Maximum Element:", max_num)

def Minimum(num_list):

    min_num = num_list[0]

    for i in num_list:

        if i < min_num:
            min_num = i

    print("Minimum Element:", min_num)

def main():

    num_list = []

    count = int(input("Enter count of numbers: "))

    for i in range(count):
        num = int(input("Enter number: "))
        num_list.append(num)

    T1 = threading.Thread(target=Maximum, args=(num_list,))
    T2 = threading.Thread(target=Minimum, args=(num_list,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from Main Thread")

if __name__ == "__main__":
    main()