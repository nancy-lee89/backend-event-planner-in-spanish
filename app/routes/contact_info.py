from flask import Blueprint, request, jsonify
from app import db
from app.models.contact_info import Contact_info
from app.models.event_info import Event_info
from .routes_helper import get_one_contact_info_or_abort

contact_info_bp = Blueprint("contact_info_bp", __name__, url_prefix="/contact_info")

# POST NEW CONTACT INFO
@contact_info_bp.route("", methods = ["POST"])
def add_contact_info():
    request_body = request.get_json()
    
    if "first_name" not in request_body or "email" not in request_body:
        return jsonify({"Details": "Missing information"}),400

    new_contact_info = Contact_info(first_name=request_body["first_name"], last_name=request_body["last_name"], email=request_body["email"])

    db.session.add(new_contact_info)
    db.session.commit()

    contact_info_dict = new_contact_info.to_dict()

    return jsonify(contact_info_dict),201

# GET THE LIST OF ALL CONTACT INFO
@contact_info_bp.route("", methods=["GET"])
def get_all_contact_info():

    contact_info_all = Contact_info.query.all()
    
    # response = [contact_info.to_dict() for contact_info in contact_info_all]

    response = []
    for contact_info in contact_info_all:
        response.append(contact_info.to_dict())
        
    return jsonify(response), 200

# GET ONE CONTACT INFO
@contact_info_bp.route("/<contact_id>", methods=["GET"])
def get_one_contact_info(contact_id):
    
    selected_contact_info = get_one_contact_info_or_abort(contact_id)
    
    return jsonify(selected_contact_info.to_dict()), 200


# DELETE ONE CONTACT INFO
@contact_info_bp.route("/<contact_id>", methods=["DELETE"])
def delete_one_contact_info(contact_id):

    selected_contact_info=  get_one_contact_info_or_abort(contact_id)
    
    db.session.delete(selected_contact_info)
    db.session.commit()

    return jsonify({"details": f'Contact Info # {contact_id} successfully deleted'}), 200
