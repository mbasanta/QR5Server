from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'Error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not Found'}), 404)

@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'Error': 'Method Not Allowed'}), 405)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'server': 'QR5 Database'});

@app.route('/upload/', methods=['POST'])
def upload():
    if not request.json:
        abort(400)
    print(request.json)
    return jsonify({'Status': 'Success'}), 202

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )
