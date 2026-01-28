"""
Searching tool endpoint
search handle
    Search Handle for the tables
    Function
        + filter
        + search target
        + instance
"""

class Search:
    def __init__(self, connection, table_name):
        self.table_name = table_name
        self.connection = connection

    def fetch_result(self, query):
        cursor = self.connection.cursor()
        print(f"Given query for search {query}")
        try:
            cursor.execute(query)
            return cursor.fetchall()  # returning isntance about DB
        except Exception as e:
            print(f"Exception raised as {e}")
            return None
    def target_search(self, anchor_info, target_cols="*"):
        col = anchor_info[0]
        val = anchor_info[1]

        if type(target_cols) == list:
            required_tables = ", ".join(target_cols)
            query = f"SELECT {required_tables} FROM {self.table_name} WHERE {cols} = '{vals}'"
        else:
            query = f"SELECT * FROM {self.table_name} WHERE {col} = '{val}'"
        target_filter = self.fetch_result(query)
        return target_filter[0]  # filter results


    def target_cols(self, targets):
        targets = ", ".join(targets)
        print(f"target : {targets}")
        query = f"SELECT {targets} FROM {self.table_name}"
        print(f"Query for search : {query}")
        result = self.fetch_result(query)
        return result


    def instance(self):
        query = f"SELECT * FROM {self.table_name}"
        result = self.fetch_result(query)
        return result
