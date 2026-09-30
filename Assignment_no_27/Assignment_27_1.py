class BookStore:
    # Class variable
    NoOfBooks = 0

    def __init__(self, Name, Author):
        # Instance variables
        self.Name = Name
        self.Author = Author
        
        # Increment class variable whenever a new object is created
        BookStore.NoOfBooks += 1

    def Display(self):
        # Display book details using the specified format
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


def main():
    print("--- BookStore Objects ---")
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display()

    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display()

if __name__ == "__main__":
    main()