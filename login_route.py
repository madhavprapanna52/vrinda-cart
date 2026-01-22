from auth.login import *
from auth.access import *
from DB.Endpoint import *
from models.User import *
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

user_endpoint = Endpoint("users")

login_page = Blueprint('login', __name__)


@login_page.route('/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':  # User verification working
        # JS Loads the data required
        data = request.get_json()
        print(f"Data fetched : {data}")
        username = data.get("username")
        password = data.get("password")

        print(f"Got username and password as : {username} and {password}")

        # Validation of user password
        log_info = {"name" : username, "password" : password}
        result = authentication(log_info, user_endpoint)

        if result:
            info = ('name', username)
            info = tuple(info)
            user = User(info, user_endpoint)  #Initiating user
            id = str(user.information["id"]) 
            token = create_auth_key(id)
            return jsonify(access_token=token), 200

        else:
            return jsonify({"msg":"Incorrect credentials"}), 401
        
    return render_template("login.html")
