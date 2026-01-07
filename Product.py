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
    def __init__(self, product_details, end_point, anchor=""):
        """
            Product Initiation with ID
            search db -- > fetch data --> Build details dictionary and call suepr initiation
        """
        self.feilds = 'name,prize,stock'.split(',')  # feilds list 
        super().__init__(product_details,end_point,feilds=self.feilds, search_anchor=anchor)  # Initiate feilds as list of column name

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


def make_bill(cart_instance, end_point):  # Final bill is ready for calculation and transaction
    """
        Fetches Name and prize of products with end_point 
    """
    final_list = []
    print(f"Cart instance fetched as : {cart_instance}")
    cart_instance = eval(cart_instance)
    for item in cart_instance:
        detail = {"id":item[0]}
        print(f"Details for product : {detail}")
        product = Product(detail, end_point, anchor="id")
        name = product.obj_information["name"]
        prize = product.obj_information["prize"]
        element = (name, prize, item[1])
        final_list.append(element) # adding for final bill
        del product
    return final_list




