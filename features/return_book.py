from features.database import execute_query, fetch_query
from datetime import date

def return_book(user_id, book_id):
    # Update return_date in transactions
    return_date = date.today()
    query = """
    UPDATE transactions 
    SET return_date = %s 
    WHERE user_id = %s AND book_id = %s AND return_date IS NULL
    """
    execute_query(query, (return_date, user_id, book_id))

    # Mark book as available
    update_query = "UPDATE books SET availability = 1 WHERE book_id = %s"
    execute_query(update_query, (book_id,))
    print(f"Book with ID {book_id} returned successfully!")
