from features.database import execute_query

def add_book(title, author, isbn, genre=None, publication_date=None):
    try:
        # Define the SQL query
        query = """
        INSERT INTO books (title, author, isbn, genre, publication_date)
        VALUES (%s, %s, %s, %s, %s)
        """
        # Parameters for the query
        params = (title, author, isbn, genre, publication_date)

        # Execute the query
        execute_query(query, params)
        
        # If successful, return True
        print(f"Book '{title}' added successfully!")
        return True
    except Exception as e:
        # Log the error and return False
        print(f"Error adding book '{title}': {e}")
        return False
