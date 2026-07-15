def main():
    marks = float(input("Enter the marks obtained: "))

    if marks < 0 or marks > 100:
        print("Invalid input: Please enter marks between 0 and 100.")
    elif marks >= 75:
        print("Grade : Distinction")
    elif marks >= 60:   
        print("Grade : First Class")
    elif marks >= 50:
        print("Grade : Second Class")
    else:
        print("Grade : Fail")

if __name__ == "__main__":
    main()
    