import threading

def even_list_sum(data):
    total = sum(x for x in data if x % 2 == 0)
    print(f"Sum of even elements: {total}")

def odd_list_sum(data):
    total = sum(x for x in data if x % 2 != 0)
    print(f"Sum of odd elements: {total}")

def main():
    try:
        size = int(input("Enter the number of elements: "))
        arr = list(map(int, input("Enter the elements separated by space: ").split()))[:size]
    except ValueError:
        print("Please enter valid integers.")
        return
        
    # Creating threads
    t1 = threading.Thread(target=even_list_sum, args=(arr,), name="EvenList")
    t2 = threading.Thread(target=odd_list_sum, args=(arr,), name="OddList")
    
    # Starting threads concurrently
    t1.start()
    t2.start()
    
    # Wait for both threads to complete
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()