from app import db

class Event_info(db.Model):
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
