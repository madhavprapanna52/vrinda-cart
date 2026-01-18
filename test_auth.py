from auth.access import *
import time


# Authentication key check up
token = create_auth_key("1")

time.sleep(8)
verify_auth_key(token)  # should pass

time.sleep(3)
verify_auth_key(token)  # should fail




