from features.database import execute_query

def update_book(book_id, title=None, author=None, genre=None, publication_date=None):
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
    
    params.append(book_id)
    query = f"UPDATE books SET {', '.join(fields)} WHERE book_id = %s"
    execute_query(query, params)
    print(f"Book with ID {book_id} updated successfully!")
