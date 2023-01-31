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


def get_event_or_abort(event_id):
    try:
        event_id = int(event_id)
    except:
        abort(make_response({"message": f"Event {event_id} invalid."}, 400))
    event_info = Event_info.query.get(event_id)
    if not event_info:
        abort(make_response({"message": f"Event {event_id} not found."}, 404))
    return event_info


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

    print(request_body)
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

# Routes Get all the events by date


# Get one event route 
@event_info_bp.route("/<event_id>", methods=["GET"])
def get_one_event(event_id):
    chosen_event = get_event_or_abort(event_id)  
    return jsonify(Event_info.to_dict(chosen_event)), 200

# Then deleted a specific event 
@event_info_bp.route("/<event_id>", methods=["delete"])
def delete_event(event_id):
    chosen_event = get_event_or_abort(event_id)
    db.session.delete(chosen_event)
    db.session.commit()
    return jsonify(f"successfully deleted {chosen_event.event_name}"), 200



# Get a patch to modify the event 
# Render the specific date and the events of true or false