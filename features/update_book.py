from features.database import execute_query

def update_book(book_id, title=None, author=None, genre=None, publication_date=None):
    try:
        # Prepare fields to update dynamically
        fields = []
        params = []

        if title:
            fields.append("title = %s")
            params.append(title)
        if author:
            fields.append("author = %s")
            params.append(author)
        if genre:
            fields.append("genre = %s")
            params.append(genre)
        if publication_date:
            fields.append("publication_date = %s")
            params.append(publication_date)

        # If no fields to update, return False
        if not fields:
            print(f"No fields to update for book ID {book_id}")
            return False

        # Append book_id to params for WHERE clause
        params.append(book_id)

        # Create the SQL query
        query = f"UPDATE books SET {', '.join(fields)} WHERE book_id = %s"

        # Execute the query
        execute_query(query, tuple(params))  # Use tuple for params
        print(f"Book with ID {book_id} updated successfully!")
        return True
    except Exception as e:
        print(f"Error updating book with ID {book_id}: {e}")
        return False
