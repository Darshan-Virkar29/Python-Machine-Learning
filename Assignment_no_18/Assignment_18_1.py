def addition(data):
    total = 0
    for num in data:
        total += num
    return total

def main():
    size = int(input("Input : Number of elements : "))
    arr = list(map(int, input("Input Elements : ").split()))[:size]
    
    result = addition(arr)
    print("Output :", result)

if __name__ == "__main__":
    main()