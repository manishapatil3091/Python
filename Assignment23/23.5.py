from multiprocessing import Pool
import math
import os

def factorial_data(n):
    return (os.getpid(), n, math.factorial(n))

def main():
    
    num_list = []

    count = int(input("Enter count of numbers: "))

    for i in range(count):
        num = int(input("Enter number: "))
        num_list.append(num)

    with Pool() as p:
        result = p.map(factorial_data, num_list)

    for pid, num, fact in result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Factorial :", fact)
        print()

if __name__ == "__main__":
    main()