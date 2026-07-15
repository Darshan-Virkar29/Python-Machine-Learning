def BinaryEquivalent(n):
    if n < 0:
        return "Invalid input: Please enter a non-negative integer."
    elif n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def main():
    n = int(input("Enter a non-negative integer: "))
    result = BinaryEquivalent(n)
    print(f"The binary equivalent of {n} is: {result}")

if __name__ == "__main__":
    main()