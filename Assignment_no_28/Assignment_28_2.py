import os

def main():
    file_name = input("Input:\n")
    
    if os.path.exists("file.txt"):
        # Explicitly' open the file
        file = open("file.txt", 'r')
        
        # Read and split the content
        content = file.read()
        words = content.split()
        
        # Explicitly close the file
        file.close()
            
        print("\nExpected Output:")
        print(f"Total number of words in {file_name} is: {len(words)}")
    else:
        print(f"Error: {file_name} does not exist.")

if __name__ == "__main__":
    main()