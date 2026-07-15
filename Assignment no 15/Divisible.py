def main():
    number = [10,20,30,40,50]
    divisible = list(filter(lambda x: x%3==0 and x%5 == 0,number))
    print(divisible)

if __name__ == "__main__":
    main()