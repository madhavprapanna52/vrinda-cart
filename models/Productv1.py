

class Product:
    def __init__(self, anchor_information, handle):
        '''
        If it exist then only we would load information from DB
        '''
        self.information = {}  # information dictionary

        self.anchor_information = anchor_information
        self.handle = handle
        self.columns = "name,price,stock".split(",")  # critical :)
        self.sync()  # Making sync at Initiation level

    def sync(self):  # BUG : Synchronisation inst working
        ''' Takes request from DB --> Updates the information dict '''
        columns = self.columns 

        status, result = self.handle.exist(self.anchor_information)

        if status:
            for k, v in zip(columns, result[0][1:]):
                self.information[k] = v  # Initiating key value
            return True # success GOAT INdenTatIon 
        else:
            return False

    def stock(self, update=-1):
        '''
        fetch current stock
        update it via update number | raise Error while stock out
        commit into DB-unit
        '''
        try:
            stock_instance = self.information["stock"]
        except Exception as e:
            return False
        # Stock update request
        stock_instance = int(stock_instance)
        updated_stock = stock_instance + update # Making update
        # stock update information
        edit_information = ("stock", updated_stock)
        
        self.handle.edit(edit_information, self.anchor_information)
        sync_request = self.sync()
