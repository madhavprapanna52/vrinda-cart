'''
    Endpoint

Model Data flow management unit
    - Making large scale operations for creation and target edits
    - Making big abstract data flow for objects at higher levels

    Search
        -Handles true if table consists of required data to search for
        - Makes ready to load data flow for frontend calls
'''
from DB.fetch import *
from DB.Execute import *
import sqlite3 as sql

path = "/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db"
connection = sql.connect(path)

class Endpoint:
    """
    Endpointgpt.com
    using searh handle and main executor for making DB handeling
    """
    def __init__(self, table_name, executor):
        self.table_name = table_name
        self.search_handle = Search(path, table_name)
        self.executor = executor

    def search(self,search_information):
        '''
            Search for row with specific information
            returns false for not finding any 

            information =>
                ("name" : "given_name") ~ column with its value for target search
        '''
        fetch = self.search_handle.target_search(search_information)
        if fetch:
            return True, fetch[0]  # result of search
        else:
            return None

    def create(self, information):
        anchor = list(information.keys())[0]
        info = (anchor, information[anchor])

        fetch = self.search(info)
        if fetch:
            print(f"Element Exists Terminating creation")
            return None
        else:
            columns = information.keys()
            values = information.values()

            columns = tuple(columns)
            values = tuple(values)

            creation_request = Task(
                query_type="i",
                table=self.table_name,
                columns=columns,
                values=values
            )
            self.executor.add(creation_request)
            print(f"Added information to the DB")

    def edit(self, edit, target):
        column = edit[0]
        value = edit[1]
        Making edit with morning theme and its cooking my eyes
        pass # to build editing part :)
