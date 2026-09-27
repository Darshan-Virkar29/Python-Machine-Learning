def Factor(No):
    for i in range(1, No + 1):
        if (No % i == 0):
            print(i)


def main():
    No = int(input("Enter a number: "))
    Factor(No)  

if __name__ == "__main__":
    main()