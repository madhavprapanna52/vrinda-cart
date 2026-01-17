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
