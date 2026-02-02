'''
User
Features
1. cart management
2. check out endpoint
'''
from DB.object import *

class User:
    '''
    Implementation details
    cart | {product_name, quantity}
    features -> add new , remove existing , update existing quantity

    transaction endpoint
    1. compute bill 
    2. fetch cart instance | refresh cart information
    3. varify payment possible | veryfy product available
    4. deduct payment --> update products stock --> write to transaction DB
    5. order fetch and display at user page required :)

    DB_Details
    User table details
        1. id, name, password , wallet
    Cart table
    Mentaining cart object differently for easy payment handle and transaction unit
        >  user_id, item_id, stock_required

    Transaction Details
    fetch from cart table for user -> form bill with product id -> send for transaction table to updat
    '''
    def __init__(self, executor_handle, anchor_information):
        columns_list = "id,name,password"
        self.handle = DObject(executor_handle, "users", columns_list, anchor_information)
        self.handle.sync()

    def checkout(self):
        
        
