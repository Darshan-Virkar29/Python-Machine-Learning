def main():
    my_strings = ["cat", "elephant", "dog", "panther", "tiger", "lion"]

    long_strings = list(filter(lambda x: len(x) > 5, my_strings))

    print(long_strings)

if __name__ == "__main__":
    main()
