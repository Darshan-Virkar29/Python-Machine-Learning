def main():
    count_evens = lambda nums: len(list(filter(lambda x: x % 2 == 0, nums)))

    my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = count_evens(my_numbers)

    print(result)

if __name__ == "__main__":
    main()