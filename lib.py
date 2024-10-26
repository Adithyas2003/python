lib = [
    {
        'id': 1,
        'book_name': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'published_year': 1813
    },
    {
        'id': 2,
        'book_name': 'Pathummayude Aadu',
        'author': 'Vaikom Muhammad Basheer',
        'published_year': 1959 
    },
    {
        'id': 3,
        'book_name': 'Randamoozham',
        'author': 'M. T. Vasudevan Nair',
        'published_year': 1984
    }
]

def display_menu():
    print("\nThe Library Management System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def add_book_library(lib):
    book_name = input("Enter the name of the book: ").strip()
    author = input("Enter the author's name: ").strip()
    published_year = input("Enter the published year: ").strip()
    
    if not published_year.isdigit() or int(published_year) < 0:
        print("Invalid year. Please enter a valid numeric value.")
        return

    # Determine the new book's ID
    new_id = max(book['id'] for book in lib) + 1 if lib else 1
    
    lib.append({
        'id': new_id,
        'book_name': book_name,
        'author': author,
        'published_year': int(published_year)
    })
    print("Book added successfully!")

def update_library(lib):
    book_name = input("Enter the name of the book to update: ").strip()
    for book in lib:
        if book['book_name'].lower() == book_name.lower():
            new_book_name = input("Enter the new name of the book: ").strip()
            new_author = input("Enter the new author's name: ").strip()
            new_published_year = input("Enter the new published year: ").strip()
        
            if not new_published_year.isdigit() or int(new_published_year) < 0:
                print("Invalid year. Please enter a valid numeric value.")
                return
            
            book['book_name'] = new_book_name
            book['author'] = new_author
            book['published_year'] = int(new_published_year)
            print("Book updated successfully!")
            return
    print("Book not found!")

def remove_library(lib):
    book_name = input("Enter the name of the book to remove: ").strip()
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
        print(f"  ID: {book['id']}")
        print(f"  Book Name: {book['book_name']}")
        print(f"  Author: {book['author']}")
        print(f"  Published Year: {book['published_year']}\n")

def search_book(lib):
    search_type = input("enter id of  ").strip()
    
    if search_type == '1':
        book_name = input("Enter the name of the book to search: ").strip()
        for book in lib:
            if book['book_name'].lower() == book_name.lower():
                print("Book found!")
                print(f"  ID: {book['id']}")
                print(f"  Book Name: {book['book_name']}")
                print(f"  Author: {book['author']}")
                print(f"  Published Year: {book['published_year']}")
                return
        print("Book not found!")
    
    elif search_type == '2':
        book_id = input("Enter the ID of the book to search: ").strip()
        
       
        if not book_id.isdigit():
            print("Invalid ID. Please enter a numeric value.")
            return
        
        book_id = int(book_id)
        for book in lib:
            if book['id'] == book_id:
                print("Book found!")
                print(f"  ID: {book['id']}")
                print(f"  Book Name: {book['book_name']}")
                print(f"  Author: {book['author']}")
                print(f"  Published Year: {book['published_year']}")
                return
        print("Book not found!")
    
    else:
        print("Invalid option. Please enter 1 or 2.")

def main():
    global lib  
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_book_library(lib)
        elif choice == '2':
            update_library(lib)
        elif choice == '3':
            remove_library(lib)
        elif choice == '4':
            view_books(lib)
        elif choice == '5':
            search_book(lib)
        elif choice == '6':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
