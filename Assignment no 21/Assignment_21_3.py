import threading

# Shared resources
shared_counter = 0
counter_lock = threading.Lock()

def increment_task(iterations):
    global shared_counter
    for _ in range(iterations):
        # Acquire lock to safely update the shared variable
        with counter_lock:
            shared_counter += 1

def main():
    num_threads = 5
    iterations_per_thread = 100000
    threads = []
    
    print(f"Starting value of counter: {shared_counter}")
    print(f"Creating {num_threads} threads. Each will increment the counter {iterations_per_thread} times.")
    
    # Create and start multiple threads
    for i in range(num_threads):
        t = threading.Thread(target=increment_task, args=(iterations_per_thread,))
        threads.append(t)
        t.start()
        
    # Wait for all threads to finish
    for t in threads:
        t.join()
        
    # Display final result
    print(f"Final value of counter: {shared_counter}")
    print(f"Expected value: {num_threads * iterations_per_thread}")

if __name__ == "__main__":
    main()