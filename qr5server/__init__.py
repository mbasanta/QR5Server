from flask import Flask, jsonify, make_response

app = Flask(__name__)

import qr5server.apiroutes
import qr5server.errorhandlers

