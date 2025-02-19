from flask import Blueprint,jsonify,request

routesBlueprint = Blueprint('routes',__name__)

from ..models import Book
from ..database.db import db
from sqlalchemy import exc

# --- CRUD Operations ---

# GET (Read all books)
@routesBlueprint.route('/api/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = [book.to_dict() for book in books]  # Convert objects to dictionaries
    return jsonify(book_list), 200

# POST (Create a new book)
@routesBlueprint.route('/api/books', methods=['POST'])
def create_book():
    try:
        new_book_data = request.get_json()
        if not new_book_data:
            return jsonify({"error": "Request body is empty"}), 400

        title = new_book_data.get('title')
        author = new_book_data.get('author')
        publication_year = new_book_data.get('publication_year')

        if not title or not author or not publication_year:
            return jsonify({"error": "Missing required fields"}), 400

        new_book = Book(title=title, author=author, publication_year=publication_year)
        db.session.add(new_book)
        db.session.commit()
        return jsonify(new_book.to_dict()), 201

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity error (e.g., duplicate title)"}), 400  # Adjust as needed

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# GET (Read a specific book)
@routesBlueprint.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict()), 200

# PUT (Update an existing book)
@routesBlueprint.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        book = Book.query.get_or_404(book_id)
        updated_book_data = request.get_json()
        if not updated_book_data:
            return jsonify({"error": "Request body is empty"}), 400

        book.title = updated_book_data.get('title', book.title)
        book.author = updated_book_data.get('author', book.author)
        book.publication_year = updated_book_data.get('publication_year', book.publication_year)

        db.session.commit()
        return jsonify(book.to_dict()), 200

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity error (e.g., duplicate title)"}), 400

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# DELETE (Delete a book)
@routesBlueprint.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    try:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500