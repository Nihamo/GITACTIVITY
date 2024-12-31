async function addBook() {
    const data = {
        title: document.getElementById('title').value,
        author: document.getElementById('author').value,
        isbn: document.getElementById('isbn').value,
        genre: document.getElementById('genre').value,
        publication_date: document.getElementById('publication_date').value,
    };

    try {
        const response = await fetch('/add-book', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Error adding book:', error);
        alert('Failed to add book.');
    }
}

async function updateBook() {
    const data = {
        book_id: document.getElementById('book_id').value,
        title: document.getElementById('new_title').value,
        author: document.getElementById('new_author').value,
        genre: document.getElementById('new_genre').value,
        publication_date: document.getElementById('new_publication_date').value,
    };

    try {
        const response = await fetch('/update-book', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Error updating book:', error);
        alert('Failed to update book.');
    }
}

async function removeBook() {
    const data = { title: document.getElementById('title').value };

    try {
        const response = await fetch('/remove-book', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Error removing book:', error);
        alert('Failed to remove book.');
    }
}

async function searchBooks() {
    const searchTerm = document.getElementById('search_term').value;

    try {
        const response = await fetch(`/search-book?term=${encodeURIComponent(searchTerm)}`);
        const resultsDiv = document.getElementById('search-results');
        resultsDiv.innerHTML = ''; // Clear previous results

        if (!response.ok) {
            const errorData = await response.json();
            resultsDiv.innerHTML = `<p>${errorData.message || 'Error fetching search results.'}</p>`;
            return;
        }

        const books = await response.json();
        if (Array.isArray(books) && books.length > 0) {
            books.forEach((book) => {
                resultsDiv.innerHTML += `
                    <p><strong>${book.title}</strong> by ${book.author} (ISBN: ${book.isbn}, Genre: ${book.genre || 'N/A'})</p>
                `;
            });
        } else {
            resultsDiv.innerHTML = '<p>No books found.</p>';
        }
    } catch (error) {
        console.error('Error fetching search results:', error);
        alert('An error occurred while searching for books.');
    }
}

async function addUser() {
    console.log('Add User button clicked');
    const data = {
        name: document.getElementById('user_name').value,
        email: document.getElementById('user_email').value,
        phone: document.getElementById('user_phone').value || null,
    };

    console.log('Data to send:', data);

    try {
        const response = await fetch('/add-user', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        console.log('Backend response:', result);
        alert(result.message);
    } catch (error) {
        console.error('Error adding user:', error);
        alert('Failed to add user.');
    }
}

async function removeUser() {
    console.log('Remove User button clicked');
    const data = {
        user_id: document.getElementById('remove_user_id').value,
    };

    console.log('Data to send:', data);

    try {
        const response = await fetch('/remove-user', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        console.log('Backend response:', result);
        alert(result.message);
    } catch (error) {
        console.error('Error removing user:', error);
        alert('Failed to remove user.');
    }
}
