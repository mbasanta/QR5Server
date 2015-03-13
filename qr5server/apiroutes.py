from flask import Flask, jsonify, request
from qr5server import app

@app.route('/', methods=['GET'])
def index():
    return jsonify({'server': 'QR5 Database'});

@app.route('/upload/', methods=['POST'])
def upload():
    if not request.json:
        abort(400)
    print(request.json)
    return jsonify({'Status': 'Success'}), 202
