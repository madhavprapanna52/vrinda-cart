from Product import *

"""
    Manage Products
    features 
        dummy db initialization
        manage whole product stock
            - Update product and sync with db
            - Delete products
            - Mange product stocks
"""

# Product DataBase
id = 1 # Global Product id generation

product_list = [
    ("laptop", 100),
    ("mouse", 10)
]

def init_db(pro_list):
    """Product list is list of (product, prize)"""
    db = {}
    for i in pro_list:
        global id
        db[id] = (i[0],i[1])
        id += 1
    return db


class Product_Manger:
    """
        Unit to Mange domain of products
        Functions
            - Init Products data base | {1:[product, stock]
    """
    def __init__(self):
        """
            Initialise DB for products
            Transact with db for initiating products and their listing

            Procedure
                Take Basic product information and build Product Object add stock information

                basic product info --> make product object --> store in db
        """
        stage_products = init_db(product_list)
        # Forming Product objects to initiate the transactions
        for id in stage_products.keys():
            product = stage_products[id]
            name = product[0]
            prize = product[1]

            # Init Product object
            product_obj = Product(name, prize, id) # Initiated product
            data_base.upload(product_obj) # Default stock of 10
