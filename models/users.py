from sqlalchemy.sql import func
from utils.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(60), nullable = False)
    number = db.Column(db.String(15), unique=True, nullable = False)
    birthday = db.Column(db.Date, nullable = False)
    username = db.Column(db.String(10), nullable = False)
    profile_image = db.Column(db.String(200))
    description = db.Column(db.String(100))
    role = db.Column(db.String(1), nullable = False)
    status = db.Column(db.String(1), nullable = False)
    created_at = db.Column(db.DateTime(), server_default=func.now(), nullable = False)
    updated_at = db.Column(db.DateTime(), server_default=func.now(), onupdate=func.current_timestamp(), nullable = False)

    def __init__(self, name, number, birthday, username, profile_image, description, role, status):
        self.profile_image = profile_image
        self.description = description
        self.username = username
        self.birthday = birthday
        self.number = number
        self.status = status
        self.name = name
        self.role = role
