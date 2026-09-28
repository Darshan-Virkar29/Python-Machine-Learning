import threading

def display_even():
    for i in range(1, 11):
        print(f"Even: {i * 2}")

def display_odd():
    for i in range(1, 11):
        print(f"Odd: {i * 2 - 1}")

def main():
    # Create threads
    t1 = threading.Thread(target=display_even, name="Even")
    t2 = threading.Thread(target=display_odd, name="Odd")
    
    # Start threads independently
    t1.start()
    t2.start()
    
    # Wait for completion
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()