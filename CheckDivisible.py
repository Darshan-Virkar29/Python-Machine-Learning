def main():
    value = int(input("Enter the Number "))

    if  value % 3 ==0 and value % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print(" Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()