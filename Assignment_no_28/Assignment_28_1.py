import os

def main():
    file_name = input("Input:\n")
    
    if os.path.exists("file.txt"):
        # Explicitly open the file
        file = open("file.txt", 'r')
        
        # Read the lines
        lines = file.readlines()
        
        # Explicitly close the file
        file.close()
            
        print("\nExpected Output:")
        print(f"Total number of lines in {file_name} is: {len(lines)}")
    else:
        print(f"Error: {file_name} does not exist.")

if __name__ == "__main__":
    main()