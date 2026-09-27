def find_maximum(data):
    if not data:
        return None
    
    max_val = data[0]
    for num in data:
        if num > max_val:
            max_val = num
    return max_val

def main():
    size = int(input("Input : Number of elements : "))
    arr = list(map(int, input("Input Elements : ").split()))[:size]
    
    result = find_maximum(arr)
    print("Output :", result)

if __name__ == "__main__":
    main()