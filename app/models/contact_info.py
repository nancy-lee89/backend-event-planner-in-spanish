from app import db

class Contact_info(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.contact_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }