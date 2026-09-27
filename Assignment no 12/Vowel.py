def VowelOrConsonant(x):
    if (x == 'a' or x == 'e'or x == 'i' or x == 'o' or x == 'u'):
        print("Vowel")
    else:
        print("Consonant")

def main():
    x = input("Enter a character: ")
    VowelOrConsonant(x) 

if __name__ == "__main__":
    main()  