"""
Searching tool endpoint
search handle
    Search Handle for the tables
    Function
        + filter
        + search target
        + instance
"""
import sqlite3 as sql

class Search:
    def __init__(self, path, table_name):
        self.table_name = table_name
        self.connection = sql.connect(path)

    def fetch_result(self, query):
        cursor = self.connection.cursor()
        print(f"Given query for search {query}")
        try:
            cursor.execute(query)
            return cursor.fetchall()  # returning isntance about DB
        except Exception as e:
            print(f"Exception raised as {e}")
            return None
    def target_search(self, anchor_info, target="name"):  # FIX : Data set flow still broken here 
        col = anchor_info[0] # anchor column
        val = anchor_info[1] # anchor value

        # search with anchor for a single specific and fetch the output
        query = f"SELECT "
        if type(target) == list:
            target = ", ".join(target)
            query += target
        else:
            query += target
        query += f" FROM {self.table_name} WHERE {col} = "
        if type(val) == int:
            query += f"{val}"
        else:
            query += f"'{val}'"
        print(f"Final search target query : {query}")
        target_filter = self.fetch_result(query)
        return target_filter  # filter results


    def target_cols(self, targets="*"):
        
        if type(targets) == list:
            targets = ", ".join(targets)

        query = f"SELECT {targets} FROM {self.table_name}"
        result = self.fetch_result(query)
        return result
