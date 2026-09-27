import threading

def even_factor_sum(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            total += i
    print(f"Sum of even factors: {total}")

def odd_factor_sum(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            total += i
    print(f"Sum of odd factors: {total}")

def main():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Creating threads
    t1 = threading.Thread(target=even_factor_sum, args=(number,), name="EvenFactor")
    t2 = threading.Thread(target=odd_factor_sum, args=(number,), name="OddFactor")
    
    # Starting threads
    t1.start()
    t2.start()
    
    # Wait for both threads to complete
    t1.join()
    t2.join()
    
    # Main thread exit message
    print("Exit from main")

if __name__ == "__main__":
    main()