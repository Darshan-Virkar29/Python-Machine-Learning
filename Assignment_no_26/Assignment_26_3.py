class Arithmetic:
    def __init__(self):
        # Initialize instance variables to 0
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter the first value (Value1): "))
        self.Value2 = float(input("Enter the second value (Value2): "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        # Handle division by zero properly
        if self.Value2 == 0:
            return "Error: Division by zero is not allowed."
        return self.Value1 / self.Value2

def main():
    # Creating multiple objects of the Arithmetic class
    print("--- Arithmetic Object 1 ---")
    a1 = Arithmetic()
    a1.Accept()
    print(f"Addition: {a1.Addition()}")
    print(f"Subtraction: {a1.Subtraction()}")
    print(f"Multiplication: {a1.Multiplication()}")
    print(f"Division: {a1.Division()}\n")

    print("--- Arithmetic Object 2 ---")
    a2 = Arithmetic()
    a2.Accept()
    print(f"Addition: {a2.Addition()}")
    print(f"Subtraction: {a2.Subtraction()}")
    print(f"Multiplication: {a2.Multiplication()}")
    print(f"Division: {a2.Division()}\n")

if __name__ == "__main__":
    main()