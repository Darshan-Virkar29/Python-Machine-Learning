def Square(No):
    Result = No * No
    return Result

def main():
    Value = int(input("Enter Number: "))

    Ret = Square(Value)
    print("Square is :",Ret)
    
if __name__ == "__main__":
    main()