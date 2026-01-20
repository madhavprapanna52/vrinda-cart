from auth.login import *
from auth.access import *
from DB.Endpoint import *
from models.User import *
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

user_endpoint = Endpoint("users")

login_page = Blueprint('login', __name__)


@login_page.route('/', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        user_name = request.form.get("username")
        password = request.form.get("password")

        # Validation of user password
        log_info = {"name" : user_name, "password" : password}
        result = authentication(log_info, user_endpoint)

        if result:
            info = ('name', user_name)
            info = tuple(info)
            user = User(info, user_endpoint)  #Initiating user
            id = str(user.information["id"]) 
            token = create_auth_key(id)
            return "working :0"

        else:
            return "Incorrect credentials :)"
        
    return render_template("login.html")
