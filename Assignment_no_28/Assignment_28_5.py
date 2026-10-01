import os

def main():
    # Accept file name and search word separated by space
    user_input = input("Input:\n").split()
    
    if len(user_input) != 2:
        print("Invalid input. Please provide the file name and the word to search.")
        return
        
    file_name = user_input[0]
    search_word = user_input[1]
    
    if os.path.exists(file_name):
        # Explicitly open the file
        file = open(file_name, 'r')
        
        content = file.read()
        words = content.split()
        
        # Explicitly close the file
        file.close()
            
        print("\nExpected Output:")
        if search_word in words:
            print(f"The word '{search_word}' is found in {file_name}.")
        else:
            print(f"The word '{search_word}' is not found in {file_name}.")
    else:
        print(f"Error: {file_name} does not exist.")

if __name__ == "__main__":
    main()