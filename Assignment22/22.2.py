from multiprocessing import Pool
import math
import os

def factorial_info(n):
    return (os.getpid(), n, math.factorial(n))

def main():
    num_list = []

    count = int(input("Enter count of numbers: "))

    for i in range(count):
        num = int(input("Enter number: "))
        num_list.append(num)

    with Pool() as p:
        result = p.map(factorial_info, num_list)

    print("Process ID\tInput\tFactorial")
    for pid, num, fact in result:
        print(pid, "\t\t", num, "\t", fact)

if __name__ == "__main__":
    main()