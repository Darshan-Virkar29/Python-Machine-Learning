class Circle:
    # Class variable initialized to 3.14
    PI = 3.14 

    def __init__(self):
        # Instance variables initialized to 0.0
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))

    def CalculateArea(self):
        # Area = PI * r^2
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        # Circumference = 2 * PI * r
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius: {self.Radius}")
        print(f"Area: {self.Area:.2f}")
        print(f"Circumference: {self.Circumference:.2f}\n")

def main():
    # Creating multiple objects of the Circle class
    print("--- Circle Object 1 ---")
    c1 = Circle()
    c1.Accept()
    c1.CalculateArea()
    c1.CalculateCircumference()
    c1.Display()

    print("--- Circle Object 2 ---")
    c2 = Circle()
    c2.Accept()
    c2.CalculateArea()
    c2.CalculateCircumference()
    c2.Display()

if __name__ == "__main__":
    main()