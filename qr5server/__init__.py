from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS
from qr5server.routes.geojson import geojson_api

app = Flask(__name__)
app.config.from_object('config.DebugConfiguration')
app.register_blueprint(geojson_api)

cors = CORS(app, allow_headers='Origin, X-Requested-With, Content-Type, Accept')

db = SQLAlchemy(app)

from qr5server import apiroutes, errorhandlers, models
