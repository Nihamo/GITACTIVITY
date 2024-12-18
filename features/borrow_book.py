from features.database import execute_query, fetch_query
from datetime import date, timedelta

def borrow_book(user_id, book_id):
    # Check book availability
    book_query = "SELECT availability FROM books WHERE book_id = %s"
    book = fetch_query(book_query, (book_id,))
    if not book or book[0]['availability'] == 0:
        print("Book not available for borrowing!")
        return

    # Borrow the book
    borrow_date = date.today()
    due_date = borrow_date + timedelta(days=14)
    query = """
    INSERT INTO transactions (user_id, book_id, borrow_date, due_date)
    VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (user_id, book_id, borrow_date, due_date))

    # Update book availability
    update_query = "UPDATE books SET availability = 0 WHERE book_id = %s"
    execute_query(update_query, (book_id,))
    print(f"Book with ID {book_id} borrowed successfully!")
