import json
import os
import tempfile
from nose.tools import assert_equal
from qr5server import app

class TestApi(object):
    '''Test our API'''

    def setup(self):
        '''Setup to run before each test'''
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def teardown(self):
        '''Teardown to run after each test'''
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_empty_db(self):
        '''Test to make sure our empty db returns nothing'''
        return_val = self.app.get('/')
        assert_equal(json.loads(return_val.data)['server'], 'QR5 Database')

    def test_upload(self):
        '''Test a small upload'''
        with open('test_upload_small.json', 'r') as uploadfile:
            upload_str = uploadfile.read().replace('\n', '')
            upload_json = json.loads(upload_str)
        expected = upload_json['features'][0]['attributes']

        response = self.app.post('/upload/', data=upload_str,
                                 content_type='application/json')
        assert_equal(response.status_code, 202)
        assert_equal(response.mimetype, 'application/json')

        records = json.loads(self.app.get('/qr5record/').data)['records']
        print len(records)

        def check_equal(key, val):
            pass
            # assert_equal(story[key], val)

    def test_pagination(self):
        pass
