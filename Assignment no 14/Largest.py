Largest =  lambda a,b,c: max(a,b,c)

def main():

    a = int(input("Enter the first number :"))
    b = int(input("Enter the Second number :"))
    c = int(input("Enter the Third number :"))

    Result = Largest(a,b,c)

    print(f"The largest of is {Result}.")

if __name__ == "__main__":
    main()