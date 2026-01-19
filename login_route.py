from auth.login import *
from DB.Endpoint import *
from models.User import *
from flask import Blueprint, render_template, request, redirect, url_for

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
        
        return f"Got result as {result} for info {log_info}"
        

        
    return render_template("login.html")
