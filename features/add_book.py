from features.database import execute_query

def add_book(title, author, isbn, genre=None, publication_date=None):
    query = """
    INSERT INTO books (title, author, isbn, genre, publication_date)
    VALUES (%s, %s, %s, %s, %s)
    """
    params = (title, author, isbn, genre, publication_date)
    execute_query(query, params)
    print(f"Book '{title}' added successfully!")
