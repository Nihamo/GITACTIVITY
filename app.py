from flask import Flask, request, jsonify, render_template
from features.add_book import add_book
from features.remove_book import remove_book
from features.update_book import update_book
from features.search_book import search_book
from features.borrow_book import borrow_book
from features.return_book import return_book
from features.manage_users import add_user, remove_user

app = Flask(__name__, template_folder='templates')  # Ensure HTML files are in the 'templates' folder

# ==================== DEFAULT ROUTE ====================

@app.route('/')
def home():
    return render_template('index.html')  # Ensure 'index.html' exists in the 'templates' folder

# ==================== BOOK MANAGEMENT ====================

@app.route('/manage_books')
def manage_books():
    return render_template('manage_books.html')  # Ensure 'manage_books.html' exists in the 'templates' folder

@app.route('/add-book', methods=['POST'])
def add_book_route():
    data = request.json
    result = add_book(
        data['title'], 
        data['author'], 
        data['isbn'], 
        data.get('genre'), 
        data.get('publication_date')
    )
    if result:
        return jsonify({'message': 'Book added successfully'})
    else:
        return jsonify({'message': 'Failed to add book'}), 400

@app.route('/remove-book', methods=['POST'])
def remove_book_route():
    try:
        data = request.json
        if not data or 'title' not in data:
            return jsonify({'message': 'Missing title'}), 400

        result = remove_book(data['title'])
        return jsonify({'message': f"Book '{data['title']}' removed successfully" if result else f"Failed to remove book '{data['title']}'"})
    except Exception as e:
        print(f"Error in /remove-book route: {e}")
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

@app.route('/update-book', methods=['POST'])
def update_book_route():
    data = request.json
    result = update_book(
        data['book_id'], 
        data.get('title'), 
        data.get('author'), 
        data.get('genre'), 
        data.get('publication_date')
    )
    if result:
        return jsonify({'message': 'Book updated successfully'})
    else:
        return jsonify({'message': 'Failed to update book'}), 400

@app.route('/search-book', methods=['GET'])
def search_book_route():
    try:
        search_term = request.args.get('term')  # Get the search term from the query string
        if not search_term:
            return jsonify({'message': 'Search term is required'}), 400

        results = search_book(search_term)
        if results:
            return jsonify(results)  # Return the list of books
        else:
            return jsonify({'message': 'No books found matching the search term'}), 404
    except Exception as e:
        print(f"Error in /search-book route: {e}")
        return jsonify({'message': 'Internal server error', 'error': str(e)}), 500

@app.route('/borrow-book', methods=['POST'])
def borrow_book_route():
    data = request.json
    result = borrow_book(data['user_id'], data['book_id'])
    return jsonify({'message': 'Book borrowed successfully' if result else 'Failed to borrow book'})

@app.route('/return-book', methods=['POST'])
def return_book_route():
    data = request.json
    result = return_book(data['user_id'], data['book_id'])
    return jsonify({'message': 'Book returned successfully' if result else 'Failed to return book'})

# ==================== USER MANAGEMENT ====================

@app.route('/manage_users')
def manage_users():
    return render_template('manage_users.html')  # Ensure 'manage_users.html' exists in the 'templates' folder

@app.route('/add-user', methods=['POST'])
def add_user_route():
    try:
        data = request.json
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'message': 'Missing required fields'}), 400

        add_user(data['name'], data['email'], data.get('phone'))
        return jsonify({'message': f"User '{data['name']}' added successfully!"})
    except Exception as e:
        print(f"Error in /add-user route: {e}")
        return jsonify({'message': 'Failed to add user', 'error': str(e)}), 500

@app.route('/remove-user', methods=['POST'])
def remove_user_route():
    try:
        data = request.json
        if not data or 'user_id' not in data:
            return jsonify({'message': 'Missing user_id'}), 400

        remove_user(data['user_id'])
        return jsonify({'message': f"User with ID {data['user_id']} removed successfully!"})
    except Exception as e:
        print(f"Error in /remove-user route: {e}")
        return jsonify({'message': 'Failed to remove user', 'error': str(e)}), 500

# ==================== ERROR HANDLING ====================

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Route not found'}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal server error'}), 500

# ==================== RUN APPLICATION ====================

if __name__ == '__main__':
    app.run(debug=True)
