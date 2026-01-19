from auth.login import *
from models.User import *
from DB.Endpoint import *

usr = Endpoint("users")

log_info = {
    "name" : "mad",
    "password" : "1234",
    "wallet" : 10,
    "cart" : ""
}

registration(log_info, usr)
print("user registered for testing")

i = {"name" : "mad", "password" : "1234"}
r = authentication(i, usr)
print("Authentication he he results ", r)
