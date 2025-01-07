from features.database import execute_query

def add_user(name, email, phone=None):
    try:
        query = """
        INSERT INTO users (name, email, phone)
        VALUES (%s, %s, %s)
        """
        execute_query(query, (name, email, phone))
        print(f"User '{name}' added successfully!")
        return True
    except Exception as e:
        print(f"Error adding user: {e}")
        return False

def remove_user(user_id):
    try:
        query = "DELETE FROM users WHERE user_id = %s"
        execute_query(query, (user_id,))
        print(f"User with ID {user_id} removed successfully!")
        return True
    except Exception as e:
        print(f"Error removing user: {e}")
        return False
