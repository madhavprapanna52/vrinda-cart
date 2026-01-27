import sqlite3 as sql
#from config import *

connection = sql.connect("/home/madhav/Projects/vrinda-cart/DB/vrinda-cart.db", check_same_thread=False)  # FIX : Very temporary 

cursor = connection.cursor()


class Endpoint:
    def __init__(self, table_name):
        self.table_name = table_name
        self.latest_changes = []  # stores latest change

    def execute(self, query, option=0):
        """
            option = 1 -> fetch output |
        """
        cursor.execute(query)  # FIX : cursor execution is reuqired to be moduler and into single threaded such that it wont mess up the execution pipeline
        connection.commit()

        if option == 1:
            output_list = cursor.fetchall()
            return output_list # fethed output
        else:
            return None

    def search(self, anchor_information, fetch_target="*"):
        """
        anchor_information : (column, value)
        """
        column = anchor_information[0]
        value = anchor_information[1]
        # Validate search information : String type needs '' cover

        query = f"select {fetch_target} from {self.table_name} where"
        if type(value) == str:
            query += f" {column} = '{value}'"
        else:
            query += f" {column} = {value}"

        #log.info(f"Executing query for searching : {query}")
        result = self.execute(query, 1) # fetch_result
        # if result have one length its target search / mass search
        if len(result) == 1:
            result = result[0]
        return result


    def fetch_instance(self, target_fetch="*"):  # tested
        """
            input : None
            output : rows affected
        """
        query = f"select {target_fetch} from {self.table_name}"  # FIX : updated with target fetch for frontend presentation :<
        instance = self.execute(query, 1)
        return instance  # DB instance fetched

    def create(self, information):  # tested
        """
            creates row with given information
            validity check : integers with int type, string with string
        """
        query = f"insert into {self.table_name}"
        feilds = tuple(information.keys())
        values = tuple(information.values())
        
        # Building final data insertion query
        query += f" {feilds} values {values}"
        self.execute(query)

        results = self.fetch_instance()

    def edit(self, target_information, edit_information):
        """
        Data flow 
            target_information : (column, value)
            edit_information : (column, value)
        """
        column = edit_information[0]
        edit = edit_information[1]
        edit_query = f"update {self.table_name} set {column} = "

        if type(edit) == str:
            edit_query += f"'{edit}'"
        else:
            edit_query += f"{edit}"

        # seting target
        target_column = target_information[0]
        target_value = target_information[1]

        edit_query += f" where {target_column} = {target_value}"
        print(f"Required inspection for final querry to load : {edit_query} ")
        self.execute(edit_query)

    def delete(self, target_id):
        query = f"delete from {self.table_name} where id = {target_id}"
        self.execute(query)
