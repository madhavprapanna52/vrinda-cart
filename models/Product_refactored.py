"""
    Product Object
    information ~ dictionary about Product

    functions
    1. stock()
            option : edit, add, remove
            data : required for edit

    2. transaction()
    fetch current money at DB --> request payment via user object --> when payment is done --> dispatch stock
"""
from DB.General_Object import *


class Product(General_Object):
    
    def __init__(self, information, endpoint):
        feilds = 'id,name,prize,stock'.split(',')
        super().__init__(information, feilds, endpoint)

    def stock(self, update=-1):  # tested
        stock = int(self.information["stock"])
        if stock < update:
            raise NotAvailableError(self.information)
        updated_stock = stock + update
        update_information = ("stock", updated_stock)
        print(f"Info before edit : {self.information}")
        self.update(update_information)
        print(f"Information update for class : {self.information}")


# Defined Exceptions
class NotAvailableError(Exception):
    def __init__(self, information):
        self.message = f"Stock out for product information : {information}"
        super().__init__(self.message)
