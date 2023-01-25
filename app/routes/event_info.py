from flask import Blueprint
from app import db
from app.models.contact_info import Contact_info
from app.models.event_info import Event_info

event_info_bp = Blueprint("event_info_bp", __name__, url_prefix="event_info")