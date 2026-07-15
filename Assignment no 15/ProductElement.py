from functools import reduce

def main():
        
    numbers = [2, 3, 4, 5]

    product = reduce(lambda x, y: x * y, numbers)

    print(product)

if __name__ == "__main__":
    main()