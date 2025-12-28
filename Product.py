"""
    Product
        variables : Name , Prize,id
    Methods
    update_data() : Updates the data and commits to db
"""
from DB_Manager import *

class Product:
    '''
    vars = name, prizem id
    id = self generated with product manager
    methods
        get product : product with respected data { Adds to db
        update product : to edit the product data 
        product_information : fetch product information form product object


    id = Generated via product Manager db extension
    '''

    def __init__(self, name, prize):
        self.name = name
        self.prize = int(prize)
        # Initiate product at database
        product_data = (name, prize)
        self.id = init_product(product_data)
        if self.id:
            print(f"DB connection initiated with id made {self.id}")
        else:
            print(f"DB Failed while initiation | with {self.id}")


    def get(self):
        '''Returns Product object'''
        return self

    def fetch_info(self):
        """
            Testing to connect to Product Manager for Geting information with fetching object from DB
            Current method : Class data fetched
            required update : Making fetch from Data base stored object
        """"
        info = f'ID : {self.id} | Product Name : {self.name} | Prize : {self.prize}'
        return info # information about product

    def fetch_name():
        return str(self.name)

    def fetch_prize():
        return str(f"{self.prize}$")
    
    def fetch_id():
        return str(self.id)

    def update(self, opt, data):
        '''
        opt : Operation [ 1: update name, 2: prize], data = required data
        output : Updating Product details
        '''
        try:
            if not(opt in (1,2)):
                raise ValueError("Undefined Operation")

            # Making Operation
            if opt == 1:
                if type(data) == type("string"):
                    self.name = data # TODO Cascade changes to DB
            elif opt == 2:
                self.prize = data # Prize updated

        except ValueError as e:
            print(f"[*] Error In operation type {e}")

