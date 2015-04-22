'''SQL Alchemy models for user'''

# pylint: disable=no-init
# pylint: disable=too-few-public-methods

from passlib.apps import custom_app_context as pwd_context
from qr5server import db

class User(db.Model):
    '''Object to hold user records'''
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(130), unique=True)
    pw_hash = db.Column(db.String(130))

    def __init__(self, email, password):
        self.email = email
        self.pw_hash = pwd_context.encrypt(password)

    def __repr__(self):
        return '<User %r>' % self.email

    def check_password(self, password):
        '''Verify password of user'''
        return pwd_context.verify(password, self.pw_hash)
