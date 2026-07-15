
from functools import reduce

def main():
    number = [1, 2, 3, 4, 5]
    Max = reduce(lambda x, y: x if x > y else y, number)
    print(Max)  

if __name__ == "__main__":
    main()