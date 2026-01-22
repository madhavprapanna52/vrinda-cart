"""
    Making Final user api-endpoint 
Functions 
1. Add to cart button function for upadating the DB
2. Make working simple transaction unit
3. Make user information fetching route only via authentication

"""

from models.User import *
from DB.Endpoint import *
from flask import Blueprint, render_template, request, jsonify
from auth.access import *

user_endpoint = Endpoint("users")

user_page = Blueprint('user',__name__)

@user_page.route('/', methods=['POST','GET'])
def cart_update():
    if request.method == "GET":
        return "I am their"
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return jsonify({"message":"No Auth head"}), 401
    try:
        token = auth_header.split(" ")[1]
        print(f"Fetched token from request as {token}")
    except IndexError:
        return jsonify({"message" : "Auth failed"}), 401

    try:
        payload = verify_auth_key(token)
        print(f"Verification payload output : {payload}")
    except Exception as e:
        return jsonify({"message" : str(e)}), 401
    
    id = payload.get("sub")

    data = request.get_json()
    quantity = data.get("quantity")
    name = data.get("name")

    # Implemting and calling our backend services for adding to cart
    info = ("id",id)  # user information
    info =tuple(info)
    user = User(info, user_endpoint)
    elem = (name, quantity)
    elem = tuple(elem)
    user.cart(2, elem)

    return jsonify({"message" : "Adding to cart"}), 200
