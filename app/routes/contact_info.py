from flask import Blueprint
from app import db
from app.models.contact_info import Contact_info
from app.models.event_info import Event_info

contact_info_bp = Blueprint("contact_info_bp", __name__, url_prefix="contact_info")