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
import json

user_endpoint = Endpoint("users")

user_page = Blueprint('cart',__name__)

@user_page.route("/", methods=['POST', 'GET'])
def user():
    return render_template("user.html")

@user_page.route('/cart/add', methods=['POST','GET'])
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

@user_page.route('/buy', methods=['POST', 'GET'])
def buy():
    """
    Final transaction endpoint for orders and making checkout for the products in cart for user
    """
    


@user_page.route('/info', methods=['GET'])
def info():
    """
        Info route fetches information about cart and order items also with cart information json pass
        REQUIRED TO CHANGE DB FOR PASSWORD STORAGE 
    """
    # BUG : Required to store password into different table at DB
    header = request.headers.get("Authorization")

    if not header:
        return jsonify({"message" : "NO Authentication"})
    try:
        token = header.split(" ")[1]
        print(f"Token fetched as {token}")
    except IndexError:
        return jsonify({"message" : "Auth failed "}), 401
    
    try:
        payload = verify_auth_key(token)
        print(f"Payload {payload}")
    except Exception as e:
        return jsonify({"message" : str(e)}), 401
    id = payload.get("sub")  # id of the authenticated user

    info = ("id", id)
    info = tuple(info)
    user = User(info, user_endpoint)  # INFO : AGAINSTT DRY BUT WITH KISS FOR NOW 
    information = user.information

    cart_dict = json.loads(information["cart"])
    cart_list = []
    for item in cart_dict.keys():
        elem = ""
        elem += str(item) # key 
        elem += f" {str(cart_dict[item])}"
        cart_list.append(elem)

    # Load final data for the frontend
    name = information["name"]
    print(f"Information fetched why not name : {name}")
    orders = ["Order1", "Order2"]  # dummy order

    return jsonify({"name" : name, "order" : orders, "cart" : cart_list}),200  # final return
