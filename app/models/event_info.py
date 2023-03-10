from app import db
import datetime


class Event_info(db.Model):
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Should we add the event_time start and end 
    event_name = db.Column(db.String)
    event_date = db.Column(db.Date)
    event_time_start = db.Column(db.DateTime)
    event_time_end = db.Column(db.DateTime)

    event_link = db.Column(db.String)

    # The api only needs the logitude and latitude for the location 
    event_latitude = db.Column(db.Numeric(precision=18, scale=10))
    event_longitude = db.Column(db.Numeric(precision=18, scale=10))
    

    # Or should we have and then find a way to post true with a specific filter 
    event_for_family = db.Column(db.Boolean, nullable=True)
    event_for_adults = db.Column(db.Boolean, nullable=True)
    event_a_concert = db.Column(db.Boolean, nullable=True)
    event_free = db.Column(db.Boolean, nullable=True)
    event_low_cost = db.Column(db.Boolean, nullable=True)


    # This can be information we give to the user say they can use it for refrence
    event_address = db.Column(db.String)
    event_city = db.Column(db.String)
    event_zipcode = db.Column(db.Integer)
    

    def to_dict(self):
        return {
                "event_id": self.event_id,
                "event_date": self.event_date, 
                "event_name" :self.event_name, 
                "event_time_start": self.event_time_start, 
                "event_time_end": self.event_time_end, 
                "event_link": self.event_link, 
                "event_latitude": float(self.event_latitude), 
                "event_longitude": float(self.event_longitude),
                "event_for_family": self.event_for_family,
                "event_for_adults": self.event_for_adults,
                "event_a_concert": self.event_a_concert, 
                "event_free": self.event_free,
                "event_low_cost": self.event_low_cost,
                "event_address" : self.event_address,
                "event_city" : self.event_city,
                "event_zipcode" : self.event_zipcode
            }
