from Product import *
from DB_endpoint import *
from User import *

product_detail = {
    "name" : "apple_watch",
    "prize" : 300,
    "stock" : 10
}

user_details = {
    "name" : "Madahv Rimal",
    "password" : "ufd78t782buybt7rt",
    "wallet" : 2000,
    "cart" : "[]"
}  # data should be list format for appending items and conversion

endpoint = DB_object("products")
user_endpoint = DB_object("users")

apple_watch = Product(product_detail, endpoint)

user1 = User(user_details, user_endpoint)
new_item = (2,2)  # want 10 applpe watch
print(user1.cart_manager(option=2, data=new_item))

