from app import db

class Contact_info(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)