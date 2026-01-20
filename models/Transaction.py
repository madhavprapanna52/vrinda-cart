"""
    Transaction unit for Managing transaction DB

    Make bill()
   Iterate products in cart instance
    Compute information and bill about product

    Pay_bill()
    Function for completing the payment via user
    Add products with user id into db for final transaction
    completes transaction
"""
from models.Product import *
from DB.Endpoint import *


class Transaction:
    """
    Handles Transaction table and its informations

    Input : cart instance
    functions
        init
        > Computes the total bill
        PAY
        > Updates the stock of products and updates transaction db with product id and user id
    """
    def __init__(self,cart_instance, transaction_endpoint, product_endpoint):
        self.product_endpoint = product_endpoint
        self.transaction_endpoint = transaction_endpoint

        # Compute bill
        self.products = list(cart_instance.keys())
        self.cart = cart_instance
        total = 0
        for product in self.products:
            p = self.init_product(product)
            price = int(p.information["prize"])
            stock = int(cart_instance[product])
            total += (price * stock)
        self.total = total
        log.info(f"Total computed for transactions : {total}")

    def endpoint(self, user_id):  # Working endpoint
        """
            Makes stock update in db and writes to transactions db
        """
        for product in self.products:
            p = self.init_product(product)
            demand = int(self.cart[product])
            p.stock(-demand)
            # DB Entry for given product_id and user_id
            p_id = p.information["id"]
            stock = self.cart[product]  # product information
            information = {"product_id" : p_id, "stock" : stock, "customer_id" : user_id}
            log.info(f"Transaction updated for the information : {information}")
            self.transaction_endpoint.create(information)  # final writeup


    def init_product(self, name):
        info = ("name", name)  # Product to initiate
        product = Product(info, self.product_endpoint)
        return product # product object

