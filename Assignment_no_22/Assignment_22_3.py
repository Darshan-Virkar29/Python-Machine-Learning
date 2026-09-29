import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Optimized prime checking
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(n):
    # Count how many primes exist from 1 to N
    count = sum(1 for i in range(1, n + 1) if is_prime(i))
    return n, count

def main():
    numbers = [10000, 20000, 30000, 40000]
    
    pool = multiprocessing.Pool()
    
    results = pool.map(count_primes, numbers)
    
    pool.close()
    pool.join()
        
    for num, count in results:
        print(f"Total prime count for {num}: {count}")

if __name__ == "__main__":
    main()