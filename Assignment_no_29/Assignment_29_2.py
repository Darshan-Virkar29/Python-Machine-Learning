import os

def main():
    file_name = input("Input:\n")
    
    print("\nExpected Output:")
    # Check if the path exists and is a file
    if os.path.exists(file_name):
        print(f"{file_name} exists.")
    else:
        print(f"{file_name} does not exist.")

if __name__ == "__main__":
    main()