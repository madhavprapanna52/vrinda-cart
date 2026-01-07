"""
    Product Object

    variables
    - name, prize and stock
    
    operations
    - transaction endpoint unit for commiting transactions 
    - filling based stock renewing system
    - fetch product information for transaction

"""
from DB_endpoint import *


class Product(General_obj):
    """
        Object to Manage Product information and operations

        Goals
        sync with DB and mentain operations reliable for transaction and inventory
    """
    def __init__(self, product_details, end_point):
        """
            Product Initiation with ID
            search db -- > fetch data --> Build details dictionary and call suepr initiation
        """
        super().__init__(product_details,end_point)

    def transaction_endpoint(self, ordered=1):  # tested working
        '''
         Product transaction endpoint
        Ensures inventory is updated with transaction to update
        updates inventory stocks of product
        '''
        stock_update = int(self.obj_information["stock"]) - ordered
        if stock_update == 0:
            log.warning(f"Stock out for product {self.obj_information["name"]}")
        edits = [("stock",stock_update)]
        self.update(edits)  # Updating DB

    def fill_stock(self, new_stocks):  # tested working
        existing_stock = int(self.obj_information["stock"])
        updated_stock = existing_stock + new_stocks
        edits = [("stock", updated_stock)]
        self.update(edits)  # Making stock update


def make_bill(cart_instance):
    for item in cart_instance:
        product = Product(item[o])  # critical : at 145 of DB_endpoint | Make id based initiation pathway in general object

