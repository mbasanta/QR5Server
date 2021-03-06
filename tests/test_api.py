'''Test cases for our API'''

# pylint: disable=no-init
# pylint: disable=no-member

import json
from tests.test_base import BaseTestCase

class TestApi(BaseTestCase):
    '''Test our API'''

    def test_empty_db(self):
        '''Test to make sure our empty db returns nothing'''
        return_val = self.get_with_auth('/', 'GET')
        self.assertEquals(json.loads(return_val.data)['server'], 'QR5 Database')

    def test_upload(self):
        '''Test a small upload'''
        with open('test_upload_small.json', 'r') as uploadfile:
            upload_str = uploadfile.read().replace('\n', '')
            upload_json = json.loads(upload_str)
        expected = upload_json['features'][0]['attributes']

        response = self.app.post('/upload/', data=upload_str,
                                 content_type='application/json')
        self.assertEquals(response.status_code, 202)
        self.assertEquals(response.mimetype, 'application/json')

        records = json.loads(self.app.get('/qr5record/').data)['records']
        self.assertEquals(len(records), 2)

        self.assertEqual(records[0]['record_id'], expected['ID'] \
            .replace('{', '').replace('}', ''))

    def test_qr5record_to_dict(self):
        '''test dictionary response for qr5record'''
        pass

    def test_qr5record_to_geojson(self):
        '''test geojson response for qr5record'''
        pass
