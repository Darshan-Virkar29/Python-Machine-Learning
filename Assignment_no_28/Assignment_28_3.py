import os

def main():
    file_name = input("Input:\n")
    
    if os.path.exists("file.txt"):
        print("\nExpected Output:")
        
        # Explicitly open the file
        file = open("file.txt", 'r')
        
        # Iterate through and print lines
        for line in file:
            print(line.strip())
            
        # Explicitly close the file
        file.close()
    else:
        print(f"Error: {file_name} does not exist.")

if __name__ == "__main__":
    main()