from features.database import fetch_query, execute_query
from datetime import date

def check_overdue():
    today = date.today()
    query = """
    SELECT t.transaction_id, t.user_id, t.book_id, t.due_date, DATEDIFF(%s, t.due_date) AS overdue_days
    FROM transactions t
    WHERE t.return_date IS NULL AND t.due_date < %s
    """
    results = fetch_query(query, (today, today))
    overdue_list = []

    for record in results:
        overdue_days = record['overdue_days']
        fine_amount = overdue_days * 5  # Example fine calculation: $5 per day
        overdue_list.append({
            "transaction_id": record['transaction_id'],
            "user_id": record['user_id'],
            "book_id": record['book_id'],
            "fine_amount": fine_amount
        })

        # Insert into overdue table
        insert_query = """
        INSERT INTO overdue (user_id, book_id, fine_amount, overdue_days)
        VALUES (%s, %s, %s, %s)
        """
        execute_query(insert_query, (record['user_id'], record['book_id'], fine_amount, overdue_days))

    return overdue_list
