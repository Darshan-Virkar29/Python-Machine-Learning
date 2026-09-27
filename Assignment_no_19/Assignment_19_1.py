import threading

def display_even():
    for i in range(1, 11):
        print(f"Even: {i * 2}")

def display_odd():
    for i in range(1, 11):
        print(f"Odd: {i * 2 - 1}")

def main():
    # Creating threads
    even_thread = threading.Thread(target=display_even, name="Even")
    odd_thread = threading.Thread(target=display_odd, name="Odd")
    
    # Starting threads
    even_thread.start()
    odd_thread.start()
    
    # Wait for both threads to complete
    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()