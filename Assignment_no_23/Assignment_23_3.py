import multiprocessing
import os

def count_even(n):
    # Count how many even numbers exist between 1 and N
    count = sum(1 for i in range(1, n + 1) if i % 2 == 0)
    return os.getpid(), n, count

def main():
    data = [1000000, 2000000, 3000000, 4000000]
    
    pool = multiprocessing.Pool()
    results = pool.map(count_even, data)
    
    pool.close()
    pool.join()
    
    for pid, num, count in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {num}")
        print(f"Even Number Count : {count}\n")

if __name__ == "__main__":
    main()