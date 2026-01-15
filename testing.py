'''
Product Manager
Core working :
    Stock Manager system 
        ~ On product request by user updates stock | Warns Empty stock
        ~ Adding New products
        ~ Deleting products
        ~ Updating Products prize

DB end points
    - connects to manage products table
    - Syncs with order management of users about products
    - mentains persistent Storage of stocks and product details
'''

from DB.Endpoint import *
from models.Product import *
from models.Transaction import *
from models.User import *

# DB objects
product_endpoint = Endpoint("products")  # fetch instance and format them

products_list = [
    {
        "name" : "Accer-Nitro-laptop",
        "prize": 68000,
        "stock": 100
    },
    {
        "name" : "Lenovo-laptop-max-prime",
        "prize": 70000,
        "stock": 20
    }
]

def list_product(products_list):  # tested working
    log.info("Products being loaded into DB")
    for product in products_list:
        initiate_product = Product(product, product_endpoint)  #initiates the Product DB
# Initiating Products
list_product(products_list)

user_info = {
"name" : "Madhav",
"password" : "janfnpa",
"wallet" : 20000000,
"cart" : '{"Accer-Nitro-laptop":1}'
}



# User information fetched for user creation
user_endpoint = Endpoint("users")
user = User(user_info, user_endpoint)  # Initiates user
print(f"User information : {user.information}")

cart_instance = json.loads(user.information["cart"])

print(f"cart instance {cart_instance}")
# transaction details
transaction_endpoint = Endpoint("transactions")
transaction = Transaction(cart_instance,transaction_endpoint, product_endpoint)

transaction.endpoint(user.information["id"])

print(f"Final total bill : {transaction.total}")
