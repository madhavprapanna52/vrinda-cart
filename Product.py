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
    def __init__(self, Data_dictionary):
        '''
        Initiate product object with dual way
            search row if found initiate from searched
            create row if not found
        '''
        name = Data_dictionary["name"]
        id = products_db.search_row("name",name)
        if id == []:
            log.warning(f"No Table with name : {name} Making product row")
            # create data dictionary
            products_db.create_row(Data_dictionary)  # tested OK



# TODO Whole DB - end point is broken and not working fix them
Data_dictionary = {
    "name" : "Laptop",
    "prize" : 1499,
    "stock" : 1000
}
mouse = Product(Data_dictionary) # Dictionary to fetch from

