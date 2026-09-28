import threading

def even_list_sum(data_list):
    # Extract even elements and calculate sum
    total = sum(x for x in data_list if x % 2 == 0)
    print(f"Sum of even elements: {total}")

def odd_list_sum(data_list):
    # Extract odd elements and calculate sum
    total = sum(x for x in data_list if x % 2 != 0)
    print(f"Sum of odd elements: {total}")

def main():
    try:
        user_input = input("Enter a list of integers separated by space: ")
        arr = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return
        
    # Create threads
    t1 = threading.Thread(target=even_list_sum, args=(arr,), name="EvenList")
    t2 = threading.Thread(target=odd_list_sum, args=(arr,), name="OddList")
    
    # Run threads concurrently
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()