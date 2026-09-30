class Demo:
    # Class variable
    Value = 0 

    def __init__(self, no1, no2):
        # Instance variables
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print(f"Fun() executing -> no1: {self.no1}, no2: {self.no2}")

    def Gun(self):
        print(f"Gun() executing -> no1: {self.no1}, no2: {self.no2}")

def main():
    # Create two objects of the Demo class
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    # Call the instance methods in the required sequence
    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()