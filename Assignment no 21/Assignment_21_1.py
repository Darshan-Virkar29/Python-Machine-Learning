import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def display_primes(data_list):
    primes = [num for num in data_list if is_prime(num)]
    print(f"[{threading.current_thread().name}] Prime numbers: {primes}")

def display_non_primes(data_list):
    non_primes = [num for num in data_list if not is_prime(num)]
    print(f"[{threading.current_thread().name}] Non-prime numbers: {non_primes}")

def main():
    try:
        user_input = input("Enter a list of integers separated by space: ")
        arr = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    # Create threads
    t1 = threading.Thread(target=display_primes, args=(arr,), name="Prime")
    t2 = threading.Thread(target=display_non_primes, args=(arr,), name="NonPrime")
    
    # Start threads
    t1.start()
    t2.start()
    
    # Wait for completion
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()