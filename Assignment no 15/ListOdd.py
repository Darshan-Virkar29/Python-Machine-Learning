def main():
    number = [1, 2, 3, 4, 5]
    Odd = list(filter(lambda x: x%2!=0,number))
    print(Odd)

if __name__ == "__main__":
    main()