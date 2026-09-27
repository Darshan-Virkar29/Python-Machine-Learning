from Arithmetic import *

def main():
    Value1 = int(input("Enter First Number :"))
    Value2 = int(input("Enter Second Number :"))

    Ret = Addition(Value1,Value2)
    print("Addition is :",Ret)

    Ret = Subtraction(Value1,Value2)
    print("Subtraction is :",Ret)

    Ret = Multiplication(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret = Division(Value1,Value2)
    print("Division is :",Ret)

if __name__ == "__main__":
    main()