import base64
import unittest
from qr5server import app, db
from qr5server.models.user import User


class BaseTestCase(unittest.TestCase):
    """A base test case for flask-tracking."""

    test_user = 'test_user'
    test_pass = 'test_pass'

    def setUp(self):
        app.config.from_object('config.TestConfiguration')
        self.app = app.test_client()
        db.create_all()
        user = User(self.test_user, self.test_pass)
        db.session.add(user)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def get_with_auth(self, url, method):
        return self.app.open(
            url,
            method=method,
            headers={
                'Authorization': 'Basic ' + base64.b64encode(self.test_user + \
                ":" + self.test_pass)
            }
        )
