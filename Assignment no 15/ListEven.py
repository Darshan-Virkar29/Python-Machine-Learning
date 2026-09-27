def main():
    number = [1, 2, 3, 4, 5]
    Even = list(filter(lambda x: x%2==0,number))
    print(Even)

if __name__ == "__main__":
    main()