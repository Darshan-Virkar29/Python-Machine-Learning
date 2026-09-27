from functools import reduce
def main():
    number = [1, 2, 3, 4, 5]
    number = reduce(lambda x, y: x + y, number)
    print(number)

if __name__ == "__main__":  
    main()