Maximum = lambda a, b: a if a > b else b

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = Maximum(num1, num2)
    print(f"The maximum of {num1} and {num2} is {result}.")

if __name__ == "__main__":
    main()