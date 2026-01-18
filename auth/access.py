from datetime import datetime, timedelta
from jose import jwt
from jose import JWTError, ExpiredSignatureError

SECRET_KEY = "SHHH"
ALGORITHM = "HS256"

class AuthError(Exception):
    def __init__(self, error):
        super().__init__(self, error)

def create_auth_key(user_id: int) -> str:
    """
    Creates a authentication key with user id for access grant
    """
    payload = {
        "sub": user_id,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(seconds=10)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_auth_key(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except Exception as e:
        print(f"Error Occured as : {e}")
    except:
        print(f"Something is terrible here :(")
