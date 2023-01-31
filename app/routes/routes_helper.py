from flask import Blueprint, request, jsonify, abort, make_response
from app import db
from app.models.contact_info import Contact_info
from app.models.event_info import Event_info

def get_one_contact_info_or_abort(contact_id):
    try:
        contact_id = int(contact_id)
    except ValueError:
        response_str = f"Invalid contact info id: {contact_id}. ID must be an integer"
        abort(make_response(jsonify({"message":response_str}), 400))
    
    matching_contact_id = Contact_info.query.get(contact_id)

    if not matching_contact_id:
        response_str = f"Contact info # {contact_id} was not found in the database."
        abort(make_response(jsonify({"message":response_str}), 404))
    
    return matching_contact_id