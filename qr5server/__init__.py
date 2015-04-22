from flask import Flask
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS
import qr5server.routes.geojson

app = Flask(__name__)
app.config.from_object('config.DebugConfiguration')
app.register_blueprint(qr5server.routes.geojson.geojson_api)

auth = HTTPBasicAuth()

cors = CORS(app, allow_headers='Origin, X-Requested-With, Content-Type, Accept')

db = SQLAlchemy(app)

from qr5server import apiroutes, errorhandlers
from qr5server.helpers.auth import verify_password, auth_error
