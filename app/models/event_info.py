from app import db

class Event_info(db.Model):
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Should we add the event_time start and end 
    event_date = db.db.Column(db.DateTime.date)
    event_time_start = db.Column(db.DateTime)
    event_time_end = db.Column(db.DateTime)

    event_link = db.Column(db.String)

    # The api only needs the logitude and latitude for the location 
    event_latitude = db.Column(db.Integer)
    event_longitude = db.Column(db.Integer)

    # Or should we have and then find a way to post true with a specific filter 
    event_for_famliy = db.Column(db.Boolean)
    event_for_adults = db.Column(db.Boolean)
    event_a_concert = db.Column(db.Boolean)
    event_free = db.Column(db.Boolean)
    event_low_cost = db.Column(db.Boolean)


    # This can be information we give to the user say they can use it for refrence
    event_address = db.Column(db.Integer)
    event_city = db.Column(db.Integer)
    event_zipcode = db.Column(db.Integer)
    

    def to_dict(self):
        return {
                "event_id": self.event_id,
                "event_date": self.event_date, 
                "event_time_start": self.event_time_start, 
                "event_time_end": self.event_time_end, 
                "event_link": self.event_link, 
                "event_latitude": self.event_latitude, 
                "event_longitude": self.event_longitude,
                "event_for_famliy": self.event_for_famliy,
                "event_for_adults": self.event_for_adults,
                "event_a_concert": self.event_a_concert, 
                "event_free": self.event_free,
                "event_low_cost": self.event_low_cost,
                "event_address" : self.event_address,
                "event_city" : self.event_city,
                "event_zipcode" : self.event_zipcode
            }
