'''
    Endpoint

Model Data flow management unit
    - Making large scale operations for creation and target edits
    - Making big abstract data flow for objects at higher levels

    Search
        - Handles true if table consists of required data to search for
        - Makes ready to load data flow for frontend calls
'''
from DB.fetch import *
import sqlite3 as sql

path = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"
connection = sql.connect(path)

class Endpoint:
    def __init__(self, table_name, executor):
        self.table_name = table_name
        self.search_handle = Search(path, table_name)
        self.executor = executor

    def search(self):
        '''
            Search for row with specific information
            returns false for not finding any 

            information =>
                {"name" : "given_name"}
        '''
        search_info = ("name", "GigaBite")
        fetch = self.search_handle.target_search(search_info)
        if fetch:
            print(f"Found required Data row as {fetch}")
        else:
            print(" Sleep now tommorow we would fix these all")
        

    


