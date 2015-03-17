from flask import Flask, jsonify, make_response
from qr5server import app

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'Error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not Found'}), 404)

@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'Error': 'Method Not Allowed'}), 405)

@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify({'Error': 'Internal Server Error'}), 500)
