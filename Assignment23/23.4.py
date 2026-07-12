from multiprocessing import Pool
import os

def count_odd(n):
    return (os.getpid(), n, (n + 1) // 2)

def main():
    
    num_list = []

    count = int(input("Enter count of numbers: "))

    for i in range(count):
        num = int(input("Enter number: "))
        num_list.append(num)

    with Pool() as p:
        result = p.map(count_odd, num_list)

    for pid, num, count in result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Odd Number Count :", count)
        print()

if __name__ == "__main__":
    main()