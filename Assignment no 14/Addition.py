Addition = lambda a,b: a + b

def main():
        
    a = int(input("Enter the first number :"))
    b = int(input("Enter the Second number :"))

    Result = Addition(a,b)

    print(f"The sum of {a} and {b} is {Result}.")

if __name__ == "__main__":
    main()