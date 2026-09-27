def Circle(radius):
    area = 3.14159 * radius ** 2
    return area


def main():
   
    radius = float(input("Enter the radius of the circle: "))

    Ret = Circle(radius)
    
    print(f"The area of the circle is: {Ret}")

if __name__ == "__main__":
    main()