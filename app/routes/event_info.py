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

    new_event = Event_info(event_date = request_body["event_date"], 
                        event_name = request_body["event_name"],
                        event_time_start = request_body["event_time_start"], 
                        event_address = request_body["event_address"],
                        event_time_end = request_body["event_time_end"],
                        event_link = request_body["event_link"],
                        event_latitude = request_body["event_latitude"],
                        event_longitude = request_body["event_longitude"],
                        event_for_family = request_body["event_for_family"],
                        event_for_adults = request_body["event_for_adults"],
                        event_a_concert = request_body["event_a_concert"],
                        event_free = request_body["event_free"],
                        event_low_cost = request_body["event_low_cost"],
                        event_city = request_body["event_city"],
                        event_zipcode = request_body["event_zipcode"])

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
@event_info_bp.route("/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    chosen_event = get_event_or_abort(event_id)
    db.session.delete(chosen_event)
    db.session.commit()
    return jsonify(f"successfully deleted {chosen_event.event_name}"), 200

# Get a patch to modify the event 
@event_info_bp.route("/<event_id>", methods=["PATCH"])
def update_event_info(event_id):
    chosen_event = get_event_or_abort(event_id)
    
    request_body = request.get_json()
    print(request_body)
    
    if "event_name" in request_body:
        chosen_event.event_name = request_body["event_name"]

    if "event_date" in request_body:
        chosen_event.event_date = request_body["event_date"]
    
    if "event_time_start" in request_body:
        chosen_event.event_time_start = request_body["event_time_start"]

    if "event_time_end" in request_body:
        chosen_event.event_time_end = request_body["event_time_end"]

    if "event_link" in request_body:
        chosen_event.event_link = request_body["event_link"]

    if "event_latitude" in request_body:
        chosen_event.event_latitude = request_body["event_latitude"]

    if "event_longitude" in request_body:
        chosen_event.event_longitude = request_body["event_longitude"]

    if "event_for_family" in request_body:
        chosen_event.event_for_family = request_body["event_for_family"]

    if "event_for_adults" in request_body:
        chosen_event.event_for_adults = request_body["event_for_adults"]

    if "event_a_concert" in request_body:
        chosen_event.event_a_concert = request_body["event_a_concert"]

    if "event_free" in request_body:
        chosen_event.event_free = request_body["event_free"]

    if "event_low_cost" in request_body:
        chosen_event.event_low_cost = request_body["event_low_cost"]

    if "event_address" in request_body:
        chosen_event.event_address = request_body["event_address"]

    if "event_city" in request_body:
        chosen_event.event_city = request_body["event_city"]

    if "event_zipcode" in request_body:
        chosen_event.event_zipcode = request_body["event_zipcode"]
    
    db.session.commit()

    return jsonify({f"message": f"Successfully replaced event with id `{event_id}`"}), 200


# Render the specific date and the events of true or false