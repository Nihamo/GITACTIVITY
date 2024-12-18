from features.add_book import add_book
from features.remove_book import remove_book
from features.update_book import update_book
from features.search_book import search_book
from features.borrow_book import borrow_book
from features.return_book import return_book
from features.manage_users import add_user, remove_user
from features.overdue_management import check_overdue

def main():
    print("Library Management System")
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. Update book details")
    print("4. Search for a book")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Add a new user")
    print("8. Remove a user")
    print("9. Check overdue books")
    print("0. Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            genre = input("Enter genre (optional): ")
            publication_date = input("Enter publication date (YYYY-MM-DD) (optional): ")
            add_book(title, author, isbn, genre, publication_date)

        elif choice == '2':
            book_id = int(input("Enter book ID to remove: "))
            remove_book(book_id)

        elif choice == '3':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title (optional): ")
            author = input("Enter new author (optional): ")
            genre = input("Enter new genre (optional): ")
            publication_date = input("Enter new publication date (YYYY-MM-DD) (optional): ")
            update_book(book_id, title, author, genre, publication_date)

        elif choice == '4':
            search_term = input("Enter book title, author, or ISBN to search: ")
            results = search_book(search_term)
            if results:
                for result in results:
                    print(result)
            else:
                print("No books found.")

        elif choice == '5':
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            borrow_book(user_id, book_id)

        elif choice == '6':
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            return_book(user_id, book_id)

        elif choice == '7':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            phone = input("Enter phone (optional): ")
            add_user(name, email, phone)

        elif choice == '8':
            user_id = int(input("Enter user ID to remove: "))
            remove_user(user_id)

        elif choice == '9':
            overdue_books = check_overdue()
            if overdue_books:
                for overdue in overdue_books:
                    print(overdue)
            else:
                print("No overdue books.")

        elif choice == '0':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

main()

