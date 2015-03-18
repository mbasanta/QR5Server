from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('id', VARCHAR(length=40), primary_key=True, nullable=False),
    Column('lat', FLOAT),
    Column('lng', FLOAT),
    Column('dfirm_feat_id', INTEGER),
    Column('dfirm_layer', VARCHAR(length=50)),
    Column('firm_panel', VARCHAR(length=255)),
    Column('error_code', VARCHAR(length=6)),
    Column('error_desc', VARCHAR(length=255)),
    Column('qc_reviewer', VARCHAR(length=30)),
    Column('qc_status', VARCHAR(length=3)),
    Column('changes_made', VARCHAR(length=30)),
    Column('changes_verified', VARCHAR(length=30)),
    Column('comments', VARCHAR(length=255)),
    Column('response', VARCHAR(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
