import multiprocessing
import math
import os

def calculate_factorial(n):
    # Calculate factorial
    fact = math.factorial(n)
    # Get the Process ID of the worker executing this task
    process_id = os.getpid()
    return process_id, n, fact

def main():
    numbers = [10, 15, 20, 25]
    
    # Create the pool
    pool = multiprocessing.Pool()
    
    results = pool.map(calculate_factorial, numbers)
    
    # Clean up the pool
    pool.close()
    pool.join()
        
    print("Display:")
    for pid, num, fact in results:
        print(f"  * Process ID: {pid}")
        print(f"  * Input Number: {num}")
        print(f"  * Factorial: {fact}\n")

if __name__ == "__main__":
    main()