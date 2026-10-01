import os

def main():
    # Accept two space-separated file names
    user_input = input("Input:\n").split()
    
    if len(user_input) != 2:
        print("Invalid input. Please provide the source and destination file names.")
        return
        
    source_file = user_input[0]
    destination_file = user_input[1]
    
    if os.path.exists(source_file):
        # Open source file in read mode
        src = open(source_file, 'r')
        file_contents = src.read()
        src.close() # Close source immediately after reading
        
        # Open destination file in write mode
        dest = open(destination_file, 'w')
        dest.write(file_contents)
        dest.close() # Close destination after writing
            
        print("\nExpected Output:")
        print(f"Contents of {source_file} copied into {destination_file}.")
    else:
        print(f"Error: Existing file '{source_file}' does not exist.")

if __name__ == "__main__":
    main()