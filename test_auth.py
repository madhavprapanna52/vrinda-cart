from auth.access import *
import time 


log_info = {
    "name" : "mad",
    "password" : "1234",
    "wallet" : 10,
    "cart" : ""
}
access = create_auth_key("2")
print(f"Authentication id made with : {access} ")

# verification unit
time.sleep(11)
verification  = verify_auth_key(str(access))
print(f"Verfication unit output : {verification}")

