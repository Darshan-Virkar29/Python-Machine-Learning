class Numbers:
    def __init__(self):
        # Accepts a number from the user and initializes Value
        while True:
            try:
                self.Value = int(input("Enter an integer value: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        # Finds all factors of the number
        factors_list = [i for i in range(1, self.Value + 1) if self.Value % i == 0]
        print(f"Factors of {self.Value}: {factors_list}")
        return factors_list

    def SumFactors(self):
        # Returns the sum of all factors
        total = sum(i for i in range(1, self.Value + 1) if self.Value % i == 0)
        return total

    def ChkPerfect(self):
        # A perfect number is a positive integer equal to the sum of its PROPER divisors
        if self.Value <= 0:
            return False
        
        # Proper divisors exclude the number itself, so subtract self.Value from total factor sum
        proper_divisor_sum = self.SumFactors() - self.Value
        return proper_divisor_sum == self.Value


def main():
    print("--- Numbers Object 1 (e.g., try 6 or 28 for Perfect Number) ---")
    num1 = Numbers()
    print(f"Is Prime? : {num1.ChkPrime()}")
    print(f"Is Perfect? : {num1.ChkPerfect()}")
    num1.Factors()
    print(f"Sum of Factors: {num1.SumFactors()}\n")

    print("--- Numbers Object 2 (e.g., try 7 or 13 for Prime Number) ---")
    num2 = Numbers()
    print(f"Is Prime? : {num2.ChkPrime()}")
    print(f"Is Perfect? : {num2.ChkPerfect()}")
    num2.Factors()
    print(f"Sum of Factors: {num2.SumFactors()}\n")

if __name__ == "__main__":
    main()