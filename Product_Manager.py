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

from DB_endpoint import *
from Product import *


# DB objects
product_endpoint = DB_object("products")  # fetch instance and format them

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
        initiate_product.info()
        del initiate_product  # saving memory 

def Bill_transaction(product_list):
    """
        Makes Final total bill
        Transaction_endpoints of product

        iterate Product list --> Initiate Product obj --> run_endpoint --> compute bill --> return bill
    """
    
