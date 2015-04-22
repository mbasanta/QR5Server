'''Routes for servicing geojson data'''

# pylint: disable=no-member

from flask import Blueprint, jsonify, abort
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import qr5server

geojson_api = Blueprint('geojson_api', __name__)  # pylint: disable=invalid-name

@geojson_api.route('/geojson/', methods=['GET'])
def geojson_list():
    '''Return all data as geojson'''
    records = qr5server.models.qr5record.QR5Record.query

    features = []
    for record in records:
        if record.lat and record.lng:
            features.append(record.to_geojson)

    return jsonify({
        'features': features,
        'type': 'FeatureCollection'
    })

@geojson_api.route('/geojson/<recordid>/', methods=['GET'])
def geojson_record(recordid):
    '''API endpoint to get a geojson by id'''
    try:
        instance = qr5server.models.qr5record.QR5Record.query \
            .filter_by(record_id=recordid).one()
        return jsonify(instance.to_geojson)
    except NoResultFound:
        abort(404)
    except MultipleResultsFound:
        abort(400)
