def display_menu():
    print("The Library Management System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def add_book_library(lib):
    book_name = input("Enter the name of the book: ")
    author = input("Enter the author's name: ")
    try:
        published_year = int(input("Enter the published year: "))
    except ValueError:
        print("Invalid year. Please enter a numeric value.")
        return
    lib.append({'book_name': book_name, 'author': author, 'published_year': published_year})
    print("Book added successfully!")

def update_library(lib):
    book_name = input("Enter the name of the book to update: ")
    for book in lib:
        if book['book_name'].lower() == book_name.lower():
            new_book_name = input("Enter the new name of the book: ")
            new_author = input("Enter the new author's name: ")
            try:
                new_published_year = int(input("Enter the new published year: "))
            except ValueError:
                print("Invalid year. Please enter a numeric value.")
                return
            book['book_name'] = new_book_name
            book['author'] = new_author
            book['published_year'] = new_published_year
            print("Book updated successfully!")
            return
    print("Book not found!")

def remove_library(lib):
    book_name = input("Enter the name of the book to remove: ")
    for i, book in enumerate(lib):
        if book['book_name'].lower() == book_name.lower():
            del lib[i]
            print("Book removed successfully!")
            return
    print("Book not found!")

def view_books(lib):
    if not lib:
        print("No books available in the library.")
        return
    for i, book in enumerate(lib, 1):
        print(f"Book {i}:")
        print(f"  Book Name: {book['book_name']}")
        print(f"  Author: {book['author']}")
        print(f"  Published Year: {book['published_year']}")
        print()

def search_book(lib):
    book_name = input("Enter the bookname of the book to search: ")
    for book in lib:
        if book['book_name'].lower() == book_name.lower():
            print("Book found!")
            print(f"  Book Name: {book['book_name']}")
            print(f"  Author: {book['author']}")
            print(f"  Published Year: {book['published_year']}")
            return
    print("Book not found!")

def main():
    lib = []
    while True:
        display_menu()
        choice= input("Enter your Choice:")
        
        if choice == '1':
            add_book_library(lib)
        elif choice == '2':
            update_library(lib)
        elif choice == '3':
            remove_library(lib)
        elif choice == '4':
            view_books(lib)
        elif choice== '5':
            search_book(lib)
        elif choice == '6':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
