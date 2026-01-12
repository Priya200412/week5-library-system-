from library_system.library import Library
from library_system.book import Book
from library_system.member import Member
def menu():
    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. View All Books")
    print("7. Save & Exit")
def main():
    library = Library()
    while True:
        menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            book = Book(
                input("Title: "),
                input("Author: "),
                input("ISBN: "),
                input("Year: ")
            )
            library.add_book(book)
            library.save_data()   
            print("Book added & saved successfully")
        elif choice == "2":
            member = Member(
                input("Name: "),
                input("Member ID: ")
            )
            library.register_member(member)
            library.save_data()  
            print("Member registered & saved successfully")
        elif choice == "3":
            result = library.borrow_book(
                input("Member ID: "),
                input("ISBN: ")
            )
            library.save_data()   
            print(result)
        elif choice == "4":
            result = library.return_book(
                input("Member ID: "),
                input("ISBN: ")
            )
            library.save_data()  
            print(result)
        elif choice == "5":
            results = library.search_books(input("Search keyword: "))
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found")
        elif choice == "6":
            if library.books:
                for book in library.books.values():
                    print(book)
            else:
                print("No books available")
        elif choice == "7":
            library.save_data()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
