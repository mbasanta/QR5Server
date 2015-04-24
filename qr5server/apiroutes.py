'''Enpoints for the QR5 api'''

# pylint: disable=no-member

from flask import jsonify, request, abort
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy import desc, asc, or_
from qr5server import app, db, auth
from qr5server.models.qr5record import QR5Record
from qr5server.helpers.argparse import argparse

@app.route('/', methods=['GET'])
@auth.login_required
def index():
    '''Place holder for landing page'''
    return jsonify({
        'server': 'QR5 Database',
        'email': auth.username()
    })

@app.route('/qr5record/', methods=['GET'])
@app.route('/qr5record/<int:page>/', methods=['GET'])
def get_records(page=1):
    '''API endpoint to get all records'''
    datapage = QR5Record.query.paginate(page,
                                        app.config.get('RECORDS_PER_PAGE'),
                                        True)

    next_page = datapage.next_num if datapage.has_next else -1
    prev_page = datapage.prev_num if datapage.has_prev else -1

    return jsonify({
        'records': [item.to_dict for item in datapage.items],
        'next_num': next_page,
        'prev_num': prev_page,
        'items': datapage.total,
        'pages': datapage.pages
    })

@app.route('/qr5record/<recordid>/', methods=['GET'])
def get_record(recordid):
    '''API endpoint to get a record by id'''
    try:
        instance = QR5Record.query.filter_by(record_id=recordid).one()
        return jsonify(instance.to_dict)
    except NoResultFound:
        abort(404)
    except MultipleResultsFound:
        abort(400)

@app.route('/datatable/', methods=['GET'])
def get_datatable():
    '''Handle datatable requests'''

    # Grab some basic parameters
    params = argparse(request.args.to_dict())
    draw = int(params['draw'])

    # Get the base query
    datapage = QR5Record.query

    # Apply sort logic
    for order in params['order'].values():
        sort_dir = desc if order['dir'] == 'desc' else asc
        sort_col = getattr(QR5Record, str(params['columns'][order['column']]['data']))
        datapage = datapage.order_by(sort_dir(sort_col))

    # Apply search logic
    search_val = str(params['search']['value'])
    if len(search_val) > 0:
        datapage = datapage.filter(or_(
            QR5Record.dfirm_layer.like('%' + search_val + '%'),
            QR5Record.firm_panel.like('%' + search_val + '%'),
            QR5Record.error_code.like('%' + search_val + '%'),
            QR5Record.error_desc.like('%' + search_val + '%'),
            QR5Record.record_id.like('%' + search_val + '%')
        ))

    # Paginate our data as needed
    length = int(params['length'])
    page = (int(params['start']) / length) + 1
    datapage = datapage.paginate(page, length, True)

    # Iterate data and ruturn datatables formatted output
    data = []
    for item in datapage.items:
        datarow = {}
        datarow['DT_RowData'] = {'pkey': item.record_id}
        datarow['dfirm_layer'] = item.dfirm_layer
        datarow['firm_panel'] = item.firm_panel
        datarow['error_code'] = item.error_code
        datarow['error_desc'] = item.error_desc

        data.append(datarow)

    return jsonify({
        'draw': draw,
        'recordsTotal': datapage.total,
        'recordsFiltered': datapage.total,
        'data': data
    })

@app.route('/upload/', methods=['POST'])
def upload():
    '''API endpoint that handles upload of qr5 data'''
    if not request.get_json() or not 'features' in request.get_json():
        abort(400)

    json = request.get_json()
    features = json['features']

    for feature in features:
        attrs = feature['attributes']
        geo = feature['geometry']
        guid = attrs['ID'].replace('{', '').replace('}', '')
        try:
            instance = QR5Record.query.filter_by(record_id=guid).one()
        except NoResultFound:
            instance = QR5Record(record_id=guid)
            db.session.add(instance)

        instance.lat = geo['y']
        instance.lng = geo['x']
        instance.dfirm_feat_id = attrs['DFIRM_Feature_ID']
        instance.dfirm_layer = attrs['DFIRM_Layer']
        instance.firm_panel = attrs['FIRM_Panel']
        instance.error_code = attrs['Error_Code']
        instance.error_desc = attrs['Error_Code_Description']
        instance.qc_reviewer = attrs['QC_Reviewer']
        instance.qc_status = attrs['QC_Status']
        instance.changes_made = attrs['Changes_Made']
        instance.changes_verified = attrs['Changes_Verified']
        instance.comments = attrs['Comments']
        instance.response = attrs['Response']

        db.session.commit()

    # app.logger.info(json['features'])

    return jsonify({'Status': 'Success'}), 202
