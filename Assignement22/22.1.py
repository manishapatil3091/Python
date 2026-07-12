from multiprocessing import Pool

def sum_of_squares(no):
    return sum(i * i for i in range(1, no + 1))

def main():
    num_list = []

    count = int(input("Enter count of numbers: "))

    for i in range(count):
        num = int(input("Enter number: "))
        num_list.append(num)

    with Pool() as p:
        result = p.map(sum_of_squares, num_list)

    print("Input :", num_list)
    print("Output:")
    for n, ans in zip(num_list, result):
        print(f"Sum of squares from 1 to {n} = {ans}")

if __name__ == "__main__":
    main()