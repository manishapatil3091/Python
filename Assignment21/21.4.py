import threading

SumResult = 0
ProductResult = 1

def SumElements(num_list):

    global SumResult
    SumResult = 0

    for num in num_list:
        SumResult = SumResult + num

def ProductElements(num_list):

    global ProductResult
    ProductResult = 1

    for num in num_list:
        ProductResult = ProductResult * num

def main():

    num_list = []

    count = int(input("Enter count of numbers: "))

    for i in range(count):
        num = int(input("Enter number: "))
        num_list.append(num)

    T1 = threading.Thread(target=SumElements, args=(num_list,))
    T2 = threading.Thread(target=ProductElements, args=(num_list,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum of Elements:", SumResult)
    print("Product of Elements:", ProductResult)

if __name__ == "__main__":
    main()