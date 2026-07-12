from multiprocessing import Pool
import os

def even_sum(n):
    total = sum(range(2, n + 1, 2))
    return (os.getpid(), n, total)

def main():
    num_list = []

    count = int(input("Enter count of numbers: "))

    for i in range(count):
        num = int(input("Enter number: "))
        num_list.append(num)

    with Pool() as p:
        result = p.map(even_sum, num_list)

    for pid, num, total in result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Sum of Even Numbers :", total)
        print()

if __name__ == "__main__":
    main()