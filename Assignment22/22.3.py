from multiprocessing import Pool
import math

def count_primes(n):
    count = 0

    for num in range(2, n + 1):
        prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            count += 1

    return count

def main():
    num_list = []

    count = int(input("Enter count of numbers: "))

    for i in range(count):
        num = int(input("Enter number: "))
        num_list.append(num)

    with Pool() as p:
        result = p.map(count_primes, num_list)

    for n, c in zip(num_list, result):
        print(f"Prime numbers between 1 and {n} = {c}")

if __name__ == "__main__":
    main()