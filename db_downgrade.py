#!/Users/mbasanta/virtualenvs/QR5Server/bin/python

from migrate.versioning import api
from config import BaseConfiguration

DATABASE_URI = BaseConfiguration.SQLALCHEMY_DATABASE_URI
MIGRATE_REPO = BaseConfiguration.SQLALCHEMY_MIGRATE_REPO

v = api.db_version(DATABASE_URI, MIGRATE_REPO)
api.downgrade(DATABASE_URI, MIGRATE_REPO, v - 1)
v = api.db_version(DATABASE_URI, MIGRATE_REPO)

print('Current database version: ' + str(v))
