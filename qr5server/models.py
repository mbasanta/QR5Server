from qr5server import db

class QR5Record(db.Model):
    record_id = db.Column(db.String(40), primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    dfirm_feat_id = db.Column(db.Integer)
    dfirm_layer = db.Column(db.String(50))
    firm_panel = db.Column(db.String(255))
    error_code = db.Column(db.String(6))
    error_desc = db.Column(db.String(255))
    qc_reviewer = db.Column(db.String(30))
    qc_status = db.Column(db.String(3))
    changes_made = db.Column(db.String(30))
    changes_verified = db.Column(db.String(30))
    comments = db.Column(db.String(255))
    response = db.Column(db.String(255))

    def __repr__(self):
        return '<QR5Record %r>' % self.id

    def serialize(self):
        '''Return object in dict for easy serialization'''
        pass
