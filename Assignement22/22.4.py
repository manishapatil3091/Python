from multiprocessing import Pool
import time

def power_sum(n):
    return sum(i**5 for i in range(1, n + 1))

def main():
    num_list = []

    count = int(input("Enter count of numbers: "))

    for i in range(count):
        num = int(input("Enter number: "))
        num_list.append(num)
    
    start_time = time.perf_counter()

    with Pool() as p:
        result = p.map(power_sum, num_list)

    end_time = time.perf_counter()

    for n, ans in zip(num_list, result):
        print(f"Sum up to {n} = {ans}")

    print(f"\n Time Required is : {end_time-start_time:.4f}")

if __name__ == "__main__":
    main()