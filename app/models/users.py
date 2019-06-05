from app.database import db
from app.database.model import ModelMixin
import sqlalchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Users(ModelMixin, db.Model, UserMixin):
    __tablename__ = 'users'
    
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))
    
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<Username: {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)