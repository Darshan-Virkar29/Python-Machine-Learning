def ChkNum(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def main():
    num = int(input("Enter a number: "))
    if ChkNum(num):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()