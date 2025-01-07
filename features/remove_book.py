from features.database import execute_query

def remove_book(title):
    try:
        query = "DELETE FROM books WHERE title = %s"
        params = (title,)
        execute_query(query, params) 
        print(f"Book with title '{title}' removed successfully!")
        return True
    except Exception as e:
        print(f"Error removing book: {e}")
        return False
