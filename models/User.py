from DB.General_Object import *
from models.Product import *
from models.Transaction import *
from config import *
import json
from config import *

class User(General_Object):
    """
        User entity
    Key functions
        Makes transactions at order level
    Issue with the cart operatioins
    """
    def __init__(self, information, endpoint):  # FIX : Self initiates required for pasword hash system for storing the password
        feilds = "id,name,password,wallet,cart".split(",")
        super().__init__(information, feilds, endpoint)
        log.info("Initiating User with information : {self.information}")
    # TODO : Update DB via sqlite3 console for making {} in cart string for this json part to work
    def cart(self, option, data):  # tested working
        """
            Making cart management system via data seriealization using json """
        cart = self.information["cart"] # raw string from DB
        print(f"cat information from frontend : {cart}")
        cart = json.loads(cart)

        if option == 1: # Adding up to existing product quantity
            target_product = data[0]  # product
            for product in cart.keys():
                cart_instance = int(cart[product])
                if product == target_product:
                    updated_instance = cart_instance + int(data[1])
                    cart[product] = updated_instance 

        elif option == 2:
            cart[data[0]] = data[1] # Adding new item

        elif option == 3:
            for product in cart.keys():
                if product == data[0]:
                    delete_target = product
            cart.pop(delete_target)

        else:
            log.warning("Critical crash")
            return 0
        # json based db load build
        cart = json.dumps(cart)  # converts to db friendly
        log.info("Cart information for final update : {cart}")
        update_cart = ("cart", cart)
        self.update(update_cart)
        return 1

