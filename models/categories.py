# from utils.db import db
from app import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Category {self.name}>'