from datetime import datetime, timedelta
from jose import jwt
from jose import JWTError, ExpiredSignatureError

SECRET_KEY = "SHHH"
ALGORITHM = "HS256"

class AuthError(Exception):
    def __init__(self, error):
        super().__init__(self, error)

def create_auth_key(user_id):
    """
    Creates a authentication key with user id for access grant
    """
    payload = {
        "sub": user_id,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(seconds=20000)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_auth_key(token: str):
    """ 
        Containsa the decription logic of authentication system
    if it could decode the key and return payload then respective id is verifyied or it would say signature expired
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception as e:
        print(f"Error Occured as : {e}")
        return False # Signature expired ;>
    except:
        print(f"Something is terrible here :(")
