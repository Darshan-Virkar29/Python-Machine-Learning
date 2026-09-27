import threading

def count_small(text):
    count = sum(1 for c in text if c.islower())
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {threading.get_native_id()}")
    print(f"Lowercase characters count: {count}\n")

def count_capital(text):
    count = sum(1 for c in text if c.isupper())
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {threading.get_native_id()}")
    print(f"Uppercase characters count: {count}\n")

def count_digits(text):
    count = sum(1 for c in text if c.isdigit())
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {threading.get_native_id()}")
    print(f"Numeric digits count: {count}\n")

def main():
    user_string = input("Enter a string: ")
    print()
    
    # Creating threads
    t1 = threading.Thread(target=count_small, args=(user_string,), name="Small")
    t2 = threading.Thread(target=count_capital, args=(user_string,), name="Capital")
    t3 = threading.Thread(target=count_digits, args=(user_string,), name="Digits")
    
    # Starting threads
    t1.start()
    t2.start()
    t3.start()
    
    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()