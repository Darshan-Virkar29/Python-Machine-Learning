Cube = lambda x: x * x * x

def main():

    num  = int(input("Enter a number: "))

    result = Cube(num)
    print(f"The cube of {num} is {result}.")

if __name__ == "__main__":
    main()