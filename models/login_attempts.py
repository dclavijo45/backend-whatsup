from sqlalchemy.sql import func
from utils.db import db

class LoginAttempts(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    number = db.Column(db.String(15), nullable = False)
    ip_address = db.Column(db.String(15), nullable = False)
    attempts = db.Column(db.Integer, nullable = False)
    device_id = db.Column(db.String(15), nullable = False)
    created_at = db.Column(db.DateTime(), server_default=func.now(), nullable = False)
    updated_at = db.Column(db.DateTime(), server_default=func.now(), onupdate=func.current_timestamp(), nullable = False)

    def __init__(self, number, ip_address, attempts, device_id):
        self.ip_address = ip_address
        self.device_id = device_id
        self.attempts = attempts
        self.number = number
