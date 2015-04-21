'''Routes for servicing geojson data'''

from flask import Blueprint

geojson_api = Blueprint('geojson_api', __name__)  #pylint: disable=invalid-name

@geojson_api.route('/geojson/', methods=['GET'])
def geojson_list():
    '''Return all data as geojson'''
    return 'Hello GeoJSON'
