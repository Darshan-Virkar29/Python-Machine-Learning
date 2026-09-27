import threading

def display_forward():
    print("Thread1 starting...")
    for i in range(1, 51):
        print(f"Thread1: {i}")
    print("Thread1 finished.\n")

def display_reverse():
    print("Thread2 starting...")
    for i in range(50, 0, -1):
        print(f"Thread2: {i}")
    print("Thread2 finished.\n")

def main():
    # Creating threads
    t1 = threading.Thread(target=display_forward, name="Thread1")
    t2 = threading.Thread(target=display_reverse, name="Thread2")
    
    # Thread synchronization: Start Thread1 and wait for it to finish
    t1.start()
    t1.join() 
    
    # Start Thread2 ONLY after Thread1 has completed
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()