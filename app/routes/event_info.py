from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.contact_info import Contact_info
from app.models.event_info import Event_info

# The Blueprint 
event_info_bp = Blueprint("event_info_bp", __name__, url_prefix="/event_info")


# Routes Get all the events by date
# Then deleted a specific event 
# Get a patch to modify the event 
# Render the specific date and the events of true or false

# Post one event:
@event_info_bp.route("", methods = ["POST"])
def add_event():
    
    request_body = request.get_json()
    if "event_date" not in request_body \
        or "event_name" not in request_body \
            or "event_time_start" not in request_body \
                or "event_address" not in request_body:
        return jsonify({"details": "Invalid data"}),400

    new_event = Event_info(event_date=request_body["event_date"], event_name=request_body["event_name"],event_time_start=request_body["event_time_start"], event_address = request_body["event_address"])


    db.session.add(new_event)
    db.session.commit()

    event_dict = new_event.to_dict()

    return jsonify(event_dict),201


# Get all events:
@event_info_bp.route("", methods = ["GET"])
def get_all_events(): 
    all_events = Event_info.query.all()
    
    response = []
    for event in all_events:
        response.append(event.to_dict())
        
    return jsonify(response), 200

