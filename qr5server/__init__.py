from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, allow_headers='Origin, X-Requested-With, Content-Type, Accept')
app.config.from_object('config.DebugConfiguration')
db = SQLAlchemy(app)

from qr5server import apiroutes, errorhandlers, models
