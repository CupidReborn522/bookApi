from .database.db import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)  # TEXT type
    author = db.Column(db.Text, nullable=False) # TEXT type
    publication_year = db.Column(db.Integer, nullable=False) # INTEGER type

    def to_dict(self):  # Helper method to convert object to dictionary
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'publication_year': self.publication_year
        }
