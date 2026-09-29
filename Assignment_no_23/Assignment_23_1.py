import multiprocessing
import os

def sum_even(n):
    # Calculate the sum of even numbers between 1 and N
    total = sum(range(2, n + 1, 2))
    return os.getpid(), n, total

def main():
    data = [1000000, 2000000, 3000000, 4000000]
    
    # Create the multiprocessing Pool explicitly
    pool = multiprocessing.Pool()
    
    # Map the function to the data list
    results = pool.map(sum_even, data)
    
    # Close the pool and wait for tasks to complete
    pool.close()
    pool.join()
    
    # Display results in the expected format
    for pid, num, total in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {num}")
        print(f"Sum of Even Numbers : {total}\n")

if __name__ == "__main__":
    main()