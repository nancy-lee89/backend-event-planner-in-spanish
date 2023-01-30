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

