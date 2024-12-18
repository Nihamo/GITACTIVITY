from features.database import fetch_query

def search_book(search_term):
    query = """
    SELECT * FROM books 
    WHERE title LIKE %s OR author LIKE %s OR isbn = %s
    """
    params = (f"%{search_term}%", f"%{search_term}%", search_term)
    results = fetch_query(query, params)
    return results
