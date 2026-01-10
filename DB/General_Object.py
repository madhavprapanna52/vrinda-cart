

class General_Object:
    '''
    Data Entity Handle object
    Handles each row, represents for whole table
    functions
        1. Creates handle for table with specific to feilds
            small query for DB-handle
        2. Initiating DB-sync object for data flow
        3.sync functions for object data flow
    '''
    def __init__(self, information, feilds, endpoint):
        '''
            information : dictionary with feilds based dataset
            feilds : id,name,...

            Note : if information is dict --> creating that column
            else : Search based initiation with information type being tuple

        '''
        self.feilds = feilds
        self.endpoint = endpoint
        # Creating object if len(information) > 1
        if type(information) == dict:
            self.endpoint.create(information)
            # search anchor for initiation
            anchor_column = list(information.keys())[0]
            anchor_value = information[anchor_column]
            search_information = (anchor_column, anchor_value)

        else:
            search_information = information
        # DB search for initiating object information
        fetch = self.endpoint.search(search_information)  # One tuple
        # Validate fetch details with feilds given for validation
        self.information = {}
        i = 0
        for e in feilds:
            self.information[e] = fetch[i]
            i += 1
    
    def update(self, edit_information):
        """
            Initiate edit at DB --> re initiate information at class
        edit_information -> (colum,value)

        BUG : Edits execution should be with id only | id is uneditable
        """
        anchor = list(self.information.keys())[0]  # Must be Id 
        value = self.information[anchor]
        target = (anchor, value)

        self.endpoint.edit(target, edit_information)
        fetch = self.endpoint.search(target)  # returns one tuple
        # Re-initialize information
        feilds = list(self.information.keys())
        i = 0
        for feild in feilds:
            self.information[feild] = fetch[i]
            i += 1
