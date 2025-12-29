"""
    Product Object
    - Manages Product level data
    Either initiate a new product or fetch from db to initiate itself
"""
from DB_endpoint import *

# Initiating DB endpoints for required objects
products_db = DB_object("products")



class Product:
    """
        features required
            1. Dual initiation logic
                - Either init from DB or make new
            2. Make Basic Crude operations
            3. Execute dataset at product level
    """
    def __init__(self, name, prize=100, stock=100):
        '''
        Initiate product object with dual way
            search row if found initiate from searched
            create row if not found
        '''
        id = products_db.search_row("name",name)
        if id:
            print(f"got id respective with details of {name} as {id}")
        else:
            print("Creating product")
        # Creating ROW
        data = {"name":name, "prize":prize, "stock":stock}
        id = products_db.create_row(data)
        self.id = id 

# testing DB
# TODO Whole DB - end point is broken and not working fix them
mouse = Product("Mouse")

