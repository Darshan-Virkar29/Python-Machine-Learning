import MarvellousNum

def ListPrime(data):
    prime_sum = 0
    for num in data:
        if MarvellousNum.ChkPrime(num):
            prime_sum += num
    return prime_sum

def main():
    size = int(input("Input : Number of elements : "))
    arr = list(map(int, input("Input Elements : ").split()))[:size]
    
    result = ListPrime(arr)
    print("Output :", result)

if __name__ == "__main__":
    main()