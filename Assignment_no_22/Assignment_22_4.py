import multiprocessing
import time

def sum_of_fifth_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 5
    return total

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]
    
    # Record the start time
    start_time = time.time()
    
    pool = multiprocessing.Pool()
    
    results = pool.map(sum_of_fifth_powers, numbers)
    
    pool.close()
    pool.join()
        
    # Record the end time
    end_time = time.time()
    
    print("Input:")
    print(f"{numbers}\n")
    
    print("Output:")
    print(f"{results}\n")
    
    # Measure and display total execution time
    execution_time = end_time - start_time
    print(f"Measure total execution time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    main()