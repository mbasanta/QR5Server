'''Authentication helpers'''

# pylint: disable=no-member

from flask import jsonify, make_response
from qr5server import auth
from qr5server.models import User

@auth.verify_password
def verify_password(email, password):
    '''Password verification handler'''
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    return user.check_password(password)

@auth.error_handler
def auth_error():
    '''
    Unauthorized access handler, We're returning a 403 error to keep the
    browser from prompting the user for a login and pw. This is an API,
    remember?
    '''
    return make_response(jsonify({'Error': 'Unauthorized access'}), 403)
