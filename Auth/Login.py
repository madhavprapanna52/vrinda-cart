"""
Simple authentication system
User information --> password hash --> store it
"""
from models.User import *
from passlib.context import CryptContext
from config import *


pwd_context = CryptContext(
    schemes=['argon2','bcrypt'],
    deprecated='auto'
)

def hash(password_string):
    return pwd_context.hash(password_string)

# Registration

"""
information_json = {
                    "name" : user_name,
                    "password" : password,
                    "wallet" : wallet_rupees,
                    "cart" : TEXT
                    }
"""

def registration(information_json, user_endpoint):
    password = information_json["password"]
    information_json["password"] = hash(password)
    user = User(information_json, user_endpoint)  # User registered
    log.info(f"User Registration completed with information : {information_json}")
    del user

def authentication(log_info, user_endpoint):
    """
    search user -> hash password -> if correct return True or False based on match
    """
    search_string = tuple(("name", log_info["name"]))
    print(f"log information : {log_info}")
    try:
        search = user_endpoint.search(search_string)  # FIX : User object have to fetch list of users while initiating
        log.info(f"[auth] user searched output : {search}")
    except Exception as e:
        print(f"Found a Exception with : {e}")
        return False
    user = User(search_string, user_endpoint)
    stored_hash = user.information["password"]
    plane_text = log_info["password"]
    result = pwd_context.verify(plane_text, stored_hash)
    return result
