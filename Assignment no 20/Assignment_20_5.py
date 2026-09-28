import threading

def display_forward():
    print("Thread1 started:")
    for i in range(1, 51):
        print(f"Thread1: {i}")
    print("Thread1 completed.\n")

def display_reverse():
    print("Thread2 started:")
    for i in range(50, 0, -1):
        print(f"Thread2: {i}")
    print("Thread2 completed.")

def main():
    # Create threads
    t1 = threading.Thread(target=display_forward, name="Thread1")
    t2 = threading.Thread(target=display_reverse, name="Thread2")
    
    # Synchronization: Start t1 and wait for it to finish completely
    t1.start()
    t1.join() 
    
    # Start t2 only after t1 has completed its execution
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()