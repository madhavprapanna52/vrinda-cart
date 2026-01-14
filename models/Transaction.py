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
from DB.General_Object import *
from models.Product import *


class Transaction(General_Object):
    """
    # BUG Transaction object cant use general object due to low resources requriements
        Information : Cart instance
        dictionary with key as product name and value as quantity
    """
    def __init__(self, information, transaction_endpoint, product_endpoint):
        self.endpoint = transaction_endpoint
        self.product_endpoint = product_endpoint
        # Fetch information about products
        products = list(information.keys())
        bill_list = []  # product_name, prize , stock required
        total_bill = 0
        for product in products:
            product_object = self.init_product(product)  # product object
            product_prize = int(product_object.information["prize"])
            stock = int(information[product])  # stock information 
            bill_element = (product, product_prize, stock)  # bill element
            bill_list.append(bill_element)  # bill builds up 
            total_bill += (product_prize * stock)
            del product_object
        self.bill_list = bill_list  # Final bill list for transaction
        self.total_bill = total_bill  # total bill 

    def product_endpoint(self):
        for element in self.bill_list:
            p = self.init_product(element[0])
            stock_change = int(element[2])
            p.stock(stock_change)  # stock update

    def init_product(self, product_name):
        info = ("name", product_name)
        product = Product(info, self.product_endpoint)
        return product



