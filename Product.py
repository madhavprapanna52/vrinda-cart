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
    An Object to handle Product
    variables : Data <-- stores all of the information
    """
    def __init__(self, Data_dictionary):
        '''
        Initiate product object with dual way
            search row if found initiate from searched
            create row if not found
        '''
        # Initiate data sets
        name = Data_dictionary["name"]
        self.info_list = []

        search_db = products_db.search_row("name",name)  # fetch id from search result
        if search_db == []:
            log.warning(f"No Table with name : {name} Making product row")
            # create Product
            products_db.create_row(Data_dictionary)
            # Now fetch information
            fetch_row = products_db.search_row("name", name)
            # Create a data to flow into class for object
            data_tuple = fetch_row[0] # tuple of data inside list
            for d in data_tuple:
                self.info_list.append(d) # adding into list
            return None 
        # initiate data for existing object
        for i in search_db[0]:
            self.info_list.append(i) # Data fetched
        print(f"Info fetched output existing Product info : {self.info_list}")
        return None

    def info(self):
        ''' Fetch product information from db via initiated objects '''
        information = f" ID : {self.info_list[0]} | Name : {self.info_list[1]} | Prize : {self.info_list[2]} | Stock : {self.info_list[3]}"
        log.info(f"Product Information fetched with Object : {information}")

    def update(self,target_id, edit_list):
        ''' Updating DB object with respective dataset of target and data
            
       edit_list : list of edits we want must list 
        Procedure
            iterate and use edit collumn to complete the edit of datapoints 
        '''
        for edit in edit_list:
            colm_name = edit[0]
            data = edit[1]
            products_db.edit_column(colm_name, data, target_id)
        log.info("Edits Executed")
        log.info(f"Edits Ouput Inspection requied : \n {products_db.fetch_instance()}")

    def delete(name):
        ''' Delete Product with respective id '''
        pass
        


# TODO Whole DB - end point is broken and not working fix them
Data_dictionary = {
    "name" : "Laptop",
    "prize" : 1499,
    "stock" : 1000
}

# TODO Make abstraction of Product to manage domains future updrade goals
Mouse = Product(Data_dictionary)
edit_list = [("name","Lallantop"),("stock",12000)]

Mouse.update(target_id=1, edit_list=edit_list)
