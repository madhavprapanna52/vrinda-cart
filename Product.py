"""
    Product
        variables : Name , Prize,id
    Methods
    update_data() : Updates the data and commits to db
"""

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

    def __init__(self, name, prize, id):
        self.name = name
        self.prize = int(prize)
        self.id = int(prize)

    def get(self):
        '''Returns Product object'''
        return self

    def fetch_info(self):
        info = f'ID : {self.id} | Product Name : {self.name} | Prize : {self.prize}'
        return info # information about product

    def fetch_name():
        return str(self.name)

    def fetch_prize():
        return str(f"{self.prize}$")

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
                    self.name = data
            elif opt == 2:
                self.prize = data # Prize updated

        except ValueError as e:
            print(f"[*] Error In operation type {e}")

