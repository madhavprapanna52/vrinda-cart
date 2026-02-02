'''
Product Model
Mentain stocks ~

adding to cart -> Reserve one stock
    * potential stock conflicts
    Checks for stock availability
        -> Warn user if stock gets ordered fasty
        -> Check once via frontend handle for stock information
        -> Outof stock returning endpoint
        -> Final transaction endpoint updates the stock number

Features
    1. stock update
    2. validating cart requirements
    3. transaction endpoint
'''
from DB.Dobject import *

class Product:
    '''
    Information flow via Dobject endpoints
    -> availability check endpoint
    -> Final transaction endpoint for products
    -> Trasaction endpoint
    '''
    def __init__(self, executor_handle, anchor_information):
        columns_list = "id,name,price,stock".split(",")  # information list
        self.handle = Dobject(executor_handle,"products", columns_list, anchor_information)
        self.handle.sync()

    def update_stock(self, update=-1):
        '''
        Make Edit request -> send to handle --> get information '''
        self.handle.sync()
        stock_instance = self.handle.information["stock"]

        valid_process = self.available(update)
        if not(valid_process):
            return False

        updated_stock = stock_instance + update
        edit_information = ("stock", updated_stock)

        self.handle.edit(edit_information)
        print(f"Edit Executed with information : {self.handle.fetch_information()}")
        return True # Executed Update



    def available(self, request):
        '''
        Fetch current stock and try to subtract if its close to zero send warning '''
        self.handle.sync()
        stock_instance = self.handle.information["stock"]

        result = stock_instance + request
        if result <= 0:
            return False
        else:
            return True


