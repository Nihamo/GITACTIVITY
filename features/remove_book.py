from features.database import execute_query

def remove_book(book_id):
    query = "DELETE FROM books WHERE book_id = %s"
    execute_query(query, (book_id,))
    print(f"Book with ID {book_id} removed successfully!")
