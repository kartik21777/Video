
from testing import db,app

class VideoMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)

with app.app_context():
    db.create_all()