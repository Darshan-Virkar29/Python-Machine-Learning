import multiprocessing
import os
import math

def calculate_factorial(n):
    # Calculate the factorial of N
    fact = math.factorial(n)
    return os.getpid(), n, fact

def main():
    data = [10, 15, 20, 25]
    
    pool = multiprocessing.Pool()
    results = pool.map(calculate_factorial, data)
    
    pool.close()
    pool.join()
    
    for pid, num, fact in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {num}")
        print(f"Factorial : {fact}\n")

if __name__ == "__main__":
    main()