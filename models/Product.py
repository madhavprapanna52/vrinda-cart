"""
    Product Object
    information ~ dictionary about Product

    functions
    1. stock()
            option : edit, add, remove
            data : required for edit

    2. transaction()
    TODO stuff -- for now not complicating transactins at product level
"""
from config import *
from DB.General_Object import *

class Product(General_Object):

    def __init__(self, information, endpoint):
        feilds = 'id,name,price,stock'.split(',')
        super().__init__(information, feilds, endpoint)
        log.info(f"Initiating Product Object : {self.information}")

    def stock(self, update=-1):  # tested
        stock = int(self.information["stock"])
        if stock < update:
            raise NotAvailableError(self.information)
        updated_stock = stock + update
        update_information = ("stock", updated_stock)
        self.update(update_information)
        log.info(f"Updating information : {self.information} with info {update}")


# Defined Exceptions
class NotAvailableError(Exception):
    def __init__(self, information):
        self.message = f"Stock out for product information : {self.information}"
        super().__init__(self.message)
