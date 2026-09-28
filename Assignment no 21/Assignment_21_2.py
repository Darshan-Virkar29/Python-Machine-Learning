import threading

def display_max(data_list):
    if data_list:
        print(f"Maximum element: {max(data_list)}")

def display_min(data_list):
    if data_list:
        print(f"Minimum element: {min(data_list)}")

def main():
    try:
        user_input = input("Enter a list of integers separated by space: ")
        arr = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    # Create threads
    t1 = threading.Thread(target=display_max, args=(arr,), name="Thread-1")
    t2 = threading.Thread(target=display_min, args=(arr,), name="Thread-2")
    
    # Start threads
    t1.start()
    t2.start()
    
    # Wait for completion
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()