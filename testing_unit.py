from Product import *
from DB_endpoint import *
from User import *


product_detail = {
    "name" : "apple_watch",
    "prize" : 2,
    "stock" : 10
}

product_detail2 = {
    "name" : "mac-book",
    "prize" : 3,
    "stock" : 10 
}


user_details = {
    "name" : "Madahv Rimal",
    "password" : "ufd78t782buybt7rt",
    "wallet" : 10,
    "cart" : "[(1,1),(2,1)]"
}  # data should be list format for appending items and conversion

user_endpoint = DB_object("users")
product_endpoint = DB_object("products")

product = Product(product_detail, product_endpoint)
pro = Product(product_detail2, product_endpoint)

user1 = User(user_details, user_endpoint)
user1.transaction_endpoint(product_endpoint)



