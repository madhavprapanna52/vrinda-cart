

class Product:
    def __init__(self, information, handle):
        '''
        If it exist then only we would load information from DB
        '''
        self.information = {}

        anchor = list(information.keys())[0]
        value = information[anchor]
        self.handle = handle

        columns = list(information.keys())

        info = [anchor, value]
        status, result = self.handle.exist(info)
        print(f"result : {result}")
        if status:
            print("Product Exist Initiation from DB")
            i = 1
            for col, val in zip(columns, result[0][1:]):
                self.information[col] = val

        else:
            print("Initiation terminated | Make Element first")
        print(f"initiation output : {self.information}")

    def stock(self, update=-1):
        print(f"Working update as {update}")



