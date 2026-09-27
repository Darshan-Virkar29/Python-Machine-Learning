def find_minimum(data):
    if not data:
        return None
        
    min_val = data[0]
    for num in data:
        if num < min_val:
            min_val = num
    return min_val

def main():
    size = int(input("Input : Number of elements : "))
    arr = list(map(int, input("Input Elements : ").split()))[:size]
    
    result = find_minimum(arr)
    print("Output :", result)

if __name__ == "__main__":
    main()