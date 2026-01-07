"""
    User object
    Manages user level things and transactions and dataset

    variables -- DB-sync
    user_name
    password_hash
    wallet
    cart

    operations
    - Validating user
    - Transactions handeling via transaction object through wallet
    - Manage cart orders
"""
from DB_endpoint import *


class User(General_obj):
    '''
        name
        hashed_password
        wallet 
        purchase history
    Initiate General DB-endpoint for making DB unit to work with

    features
    1. sotring sync data about user
    2. mentain transaction table about transactions
    3. Fetch user transactions from DB-endpoint - iNstance
    4. Make mechanism for final cart --> purchaase --> wallet update --> stock update
    '''
    def __init__(self, user_details, end_point):
        """
            user_details
            name : user_name
            hashed_password : string hashed password
            wallet : integer rupees

        Purchase history is stored in different table for lookup
        """
        super().__init__(user_details, end_point)
        # Initiate transaction endpoint to store the transactions and initiate products list for stock refle

    def cart_manager(self, option, data=""):
        """
            options based operation
        1 : fetch cart instance
        2 : adding to cart the item
        3 : removing item from cart
        4 : updating stocks

        Check at cart stage for stock out or block at frontend to buy empty items

        cart storage system
        Making string of cart information about user
        format ->  dictionary based product name , prize and stock
        initiating different DB-instances for users or storing with string based

        Initiate cart thing when user selects any products

        cart storage format
        [
        (product_id : id, quantity : number), ...
        ]
        """
        cart_instance = list(self.obj_information["cart"])

        update_instance = ""
        edit_list = [("cart", str(update_instance))]

        if option == 1:
            cart_instance = self.obj_information["cart"]
            return cart_instance
        elif option == 2:
            new_item = tuple(data)  # data contains tuple of product id and prize
            cart_instance.append(new_item)
            update_instance = str(cart_instance)
            self.update(edit_list)  # making edits list
            log.info("Edits for cart is requested through User object")
            return None
        elif option == 3:
            del cart_instance[data]  # data is tuple of object to delete
            update_instance = str(cart_instance)
            self.update(edit_list)  # Deleted cart is updated in cart DB
            log.info("cart instance is updated via deleting a product")
            return None
        elif option == 4:
            for info in cart_instance:
                if info[0] == data[0]:
                    info = list(info)
                    info[1] = data[1]  # made the edit
                    info = tuple(info)
            # info edited now commiting changes
            update_instance = cart_instance
            self.update(edit_list)
            log.info("edited the stock quantity of the user")
            return None
        else:
            print("Kharab hai cart ka code , sahi kro usko")
            


            

    def transaction_endpoint(self, final_cart_information):
        """
            Initiating final cart transaction
        Update user wallet and run cascade of other operations
        Iterate all products and initiate their transaction endpoint, fetch prize
        Build final bill, hit transaction DB table to update about user purchase
        """
        return 1 # if everything worked well
 
