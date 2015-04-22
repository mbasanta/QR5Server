#!/Users/mbasanta/virtualenvs/QR5Server/bin/python

from migrate.versioning import api
from qr5server import db
import os.path
from config import BaseConfiguration

DATABASE_URI = BaseConfiguration.SQLALCHEMY_DATABASE_URI
MIGRATE_REPO = BaseConfiguration.SQLALCHEMY_MIGRATE_REPO

db.create_all()

if not os.path.exists(MIGRATE_REPO):
    api.create(MIGRATE_REPO, 'database repository')
    api.version_control(DATABASE_URI, MIGRATE_REPO)
else:
    api.version_control(DATABASE_URI,
                        MIGRATE_REPO,
                        api.version(MIGRATE_REPO))
