def Calculatelwa(length, width):
    return length * width

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    area = Calculatelwa(length, width)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()