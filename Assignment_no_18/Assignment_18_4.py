def find_frequency(data, target):
    count = 0
    for num in data:
        if num == target:
            count += 1
    return count

def main():
    size = int(input("Input : Number of elements : "))
    arr = list(map(int, input("Input Elements : ").split()))[:size]
    search_element = int(input("Element to search : "))
    
    result = find_frequency(arr, search_element)
    print("Output :", result)

if __name__ == "__main__":
    main()