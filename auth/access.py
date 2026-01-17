"""
Simple sessions management system
* Generate a unique auth key for access of services in website
"""
from itsdangerous import URLSafeTimedSerializer
import time

# serret key
secret_key = "secret"
serializer = URLSafeTimedSerializer(secret_key)

def generate_token(usr_id, expiration_time=2):
    token_data = {"id" : usr_id}
    token = serializer.dumps(token_data, salt='access-token-salt')
    return token, expiration_time 

def token_verification(token, expiration_time=2):
    try:
        data = serializer.loads(
            token,
            salt='access-token-salt',
            max_age = expiration_time
        )
        return data['id'] # returns id if valid
    except (itsdangerous.SignatureExpired, itsdangerous.BadTimeSignature, itsdangerous.BadSignature) as e:
        print("Token verification failed :)")
        return None

