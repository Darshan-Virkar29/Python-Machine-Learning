import multiprocessing

def sum_of_squares(n):
    # Using a loop to simulate a CPU-bound task for multiprocessing
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]
    
    # Create a multiprocessing Pool explicitly
    pool = multiprocessing.Pool()
    
    # Map the function to the list of inputs
    result = pool.map(sum_of_squares, numbers)
    
    # Close the pool and wait for the work to finish
    pool.close()
    pool.join()
        
    print(f"Input\n{numbers}\n")
    print(f"Expected Output\n{result}")

if __name__ == "__main__":
    main()