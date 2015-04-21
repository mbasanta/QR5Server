from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS
import qr5server.routes.geojson

app = Flask(__name__)
app.config.from_object('config.DebugConfiguration')
app.register_blueprint(qr5server.routes.geojson.geojson_api)

cors = CORS(app, allow_headers='Origin, X-Requested-With, Content-Type, Accept')

db = SQLAlchemy(app)

from qr5server import apiroutes, errorhandlers, models
