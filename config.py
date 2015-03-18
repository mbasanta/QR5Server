'''Application Configuration'''

import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# SQL Alchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')

# Pagination
RECORDS_PER_PAGE = 10
