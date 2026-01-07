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
from Product import *
from Transaction import *


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
    def __init__(self, user_details, end_point, search_anchor="id"):
        """
            user_details
            name : user_name
            hashed_password : string hashed password
            wallet : integer rupees

        Purchase history is stored in different table for lookup
        """
        self.feilds = "name,password,wallet,cart".split(',')
        super().__init__(user_details, end_point, feilds=self.feilds)
        # Initiate transaction endpoint to store the transactions and initiate products list for stock refle
    
    def pay(self, amount):
        balance = int(self.obj_information["wallet"])
        if balance - amount > 0:
            new_balance = balance - amount
            edit_list = [("wallet",new_balance)]
            self.update(edit_list)  # BUG update the object information also
            log.info("Transaction debited from user account")
            return 1 # deducted from user wallet
        else:
            log.info("Balance Not sufficient")
            return 0


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

        Cart operations working fine
        """
        cart_instance = eval(self.obj_information["cart"])
        increment_querry = False
        # Cart Incremental update
        
        for i in range(0,len(cart_instance)):
            element = list(cart_instance[i])
            if element[0] == data[0]:
                increment_querry = True
                element[1] = int(element[1])
                element[1] += int(data[1])
                cart_instance[i] = tuple(element)  # final incerstion to the cart_instance
        print(f"Incremental check results : {cart_instance}")

        if option == 1:
            return cart_instance
        if option == 2 and not(increment_querry):
            cart_instance.append(data)
        if option == 3:
            for i in range(0,len(cart_instance)):
                elem = cart_instance[i]
                if elem[0] == data[0]:
                    cart_instance.remove(elem)

            print(f"Deleted cart_instance : {cart_instance}")
        edit_list = [("cart", str(cart_instance))]  # final edit list as per options
        print(f"Edit list for updating : {edit_list}")
        self.update(edit_list)

            

    def transaction_endpoint(self, product_endpoint):
        """
            Initiating final cart transaction
        Update user wallet and run cascade of other operations
        Iterate all products and initiate their transaction endpoint, fetch prize
        Build final bill, hit transaction DB table to update about user purchase

        final_transaction_list = [ (product_name, prize, quantity) ...]
        """
        final_transaction_list = []
        cart_instance = self.obj_information["cart"]

        final_bill = make_bill(cart_instance, product_endpoint)
        # Compute final and make transaction
        total = 0
        for elem in final_bill:
            amount = int(elem[1]) * int(elem[2])
            total += amount
        # check feasibility
        print(f"Final bill total : {total}")
        if self.pay(total):
            log.info("Payment successfull for products on the way")
            # run post payment methods
            make_bill(cart_instance, product_endpoint, stock_update=True)
            # transaction db sync  -- transaction endpoint to implement
            user_id = self.obj_information["id"]
            products_list = cart_instance
            transation_final = {"user_id":user_id, "bill":products_list}
            transaction_endpoint = DB_object("transactions")

            # Implement transaction end point
            print(f"Details : {products_list}")
            products_list = eval(products_list)
            transaction_db(products_list, user_id, transaction_endpoint)


        else:
            log.info("Transaction terminated")



 
