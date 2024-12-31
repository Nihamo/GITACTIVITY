# GIT ACTIVITY: LIBRARY MANAGEMENT SYSTEM

## Overview
The **LMS** project is a Python-based Library Management System designed to simplify and automate the management of books, users, and borrowing/returning operations in a library. It is modular, and extensible, and provides the core functionalities required for managing a library efficiently.

## Features
- **Add Book:** Add new books to the library's inventory.
- **Borrow Book:** Manage borrowing operations and track borrowed books.
- **Return Book:** Handle the return process of borrowed books.
- **Search Book:** Search for books using various criteria like title, author, etc.
- **Update Book:** Update details of existing books in the library.
- **Remove Book:** Remove books that are no longer available.
- **Overdue Management:** Track overdue books and penalties for delayed returns.
- **User Management:** Manage user details, roles, and access permissions.
- **Database Integration:** Centralized storage for books, users, and transaction records.

## File Structure
```
features/
    __pycache__/              # Compiled Python files
    add_book.py               # Handles adding new books
    borrow_book.py            # Manages borrowing operations
    config.py                 # Configuration and constants
    database.py               # Database connection and operations
    manage_users.py           # Handles user management
    overdue_management.py     # Tracks overdue books and penalties
    remove_book.py            # Removes books from the inventory
    return_book.py            # Manages book returns
    search_book.py            # Implements search functionality
    update_book.py            # Updates book information
run.py                        # Entry point for the application
README.md                     # Documentation for the project
```

## Getting Started

### Prerequisites
Ensure the following are installed on your system:
- Python 3.8 or above
- Required Python libraries (listed in `requirements.txt`)

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/GITACTIVITY.git
   cd GITACTIVITY
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To start the application, execute the following command:
```bash
python run.py
```
Follow the on-screen instructions to interact with the system.

## Functionalities

1. **Book Management**:
   - Add, search, update, and remove books in the library's inventory.

2. **Borrowing and Returning**:
   - Borrow books by specifying the user and book details.
   - Return books while updating the records accordingly.

3. **Overdue Tracking**:
   - Monitor overdue books and notify users about penalties for delayed returns.

4. **User Management**:
   - Add and manage library users, assign roles, and control access permissions.

## Contributing
We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

For detailed guidelines, refer to `CONTRIBUTING.md` (if available).

## Team Members
- Nihareeka
- Hoor
- Ishika
- Lekhya

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Inspiration for this project stems from the need for efficient library systems.
- Thanks to all contributors and open-source tools that made this project possible.
