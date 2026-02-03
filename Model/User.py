from DB.Dobject import *
#from Model.Cart import *
#from Model.Order import *

'''
User Object
Functions 
    + fetch cart information
    + fetch order history
'''

class User:
    '''
    Handles Information flow for User '''
    def __init__(self, values, executor):
        columns_list = "id,name,password".split(",")
        anchor = (columns_list[1], values[0])  # strictly with name
        self.handle = Dobject(executor, "users", columns_list, anchor)

        # Connect Object to DB
        self.handle.fetch_information()
        user_id = self.handle.fetch_information()["id"]
        print(f"Fetched User ID , {user_id}")

        #self.cart = Cart(user_id)
        #self.order = Order(user_id)

    def get_cart(self):
        pass


