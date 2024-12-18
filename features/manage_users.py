from features.database import execute_query

def add_user(name, email, phone=None):
    query = """
    INSERT INTO users (name, email, phone)
    VALUES (%s, %s, %s)
    """
    execute_query(query, (name, email, phone))
    print(f"User '{name}' added successfully!")

def remove_user(user_id):
    query = "DELETE FROM users WHERE user_id = %s"
    execute_query(query, (user_id,))
    print(f"User with ID {user_id} removed successfully!")
