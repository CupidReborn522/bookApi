from flask_sqlalchemy import SQLAlchemy

# initialize the app with the extension
db = SQLAlchemy()

# General class for models
class BaseModelMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    @classmethod
    def get_all(cls):
        return cls.query.all()
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()