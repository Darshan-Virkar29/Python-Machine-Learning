def Cube(No):
    Result = No ** 3
    return Result

def main():
    Value = int(input("Enter Number: "))

    Ret = Cube(Value)
    print("Cube is :",Ret)
    
if __name__ == "__main__":
    main()