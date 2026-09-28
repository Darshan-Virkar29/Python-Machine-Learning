import threading

def compute_sum(data_list, results_dict):
    results_dict['sum'] = sum(data_list)

def compute_product(data_list, results_dict):
    product = 1
    for num in data_list:
        product *= num
    results_dict['product'] = product

def main():
    try:
        user_input = input("Enter a list of integers separated by space: ")
        arr = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    # Dictionary to hold return values from threads
    thread_results = {}

    # Create threads, passing the shared dictionary
    t1 = threading.Thread(target=compute_sum, args=(arr, thread_results), name="Thread-1")
    t2 = threading.Thread(target=compute_product, args=(arr, thread_results), name="Thread-2")
    
    # Start threads
    t1.start()
    t2.start()
    
    # Wait for both to finish completely
    t1.join()
    t2.join()
    
    # Main thread displaying the returned results
    print("\n--- Results fetched in Main Thread ---")
    print(f"Sum of elements: {thread_results.get('sum')}")
    print(f"Product of elements: {thread_results.get('product')}")

if __name__ == "__main__":
    main()