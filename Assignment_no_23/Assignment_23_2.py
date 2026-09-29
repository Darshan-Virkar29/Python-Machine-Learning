import multiprocessing
import os

def sum_odd(n):
    # Calculate the sum of odd numbers between 1 and N
    total = sum(range(1, n + 1, 2))
    return os.getpid(), n, total

def main():
    data = [1000000, 2000000, 3000000, 4000000]
    
    pool = multiprocessing.Pool()
    results = pool.map(sum_odd, data)
    
    pool.close()
    pool.join()
    
    for pid, num, total in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {num}")
        print(f"Sum of Odd Numbers : {total}\n")

if __name__ == "__main__":
    main()