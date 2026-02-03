import os
import sqlite3 as sql

def executor(query, data="", fetch=False):
    with sql.connect(path) as connection:
        cursor = connection.cursor()
        try:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            if fetch:
                return cursor.fetchall()  # returning the result of execution
            return 1  # Success making Execution
        except Exception as e:
            print(f"Exception Occured as {e}")
            return 0


class QueryBuilder:
    def __init__(self, table_name):
        self.table = table_name

    def create(self, columns):
        column_string = ", ".join(columns)
        placeholder = ", ".join(["?"] * len(columns))

        query = f"insert into {self.table} ({column_string}) values ({placeholder})"
        return query
    
    def edit(self, target_column:str, condition_information:str):
        column = condition_information
        query = f'update {self.table} set {target_column} = ? where {column} = ?'
        return query

    def delete(self, condition_column:str):
        query = f"delete from {self.table} where {condition_column} = ?"
        return query  # requires the condition value at execution
    
    def instance(self, required_columns="*", condition_string=""):

        if type(required_columns) == list:
            required_columns = ", ".join(required_columns)
        query = f"select {required_columns} from {self.table}"
        # if condition is given we would fetch target information
        if len(condition_string) > 1:
            query += f" where {condition_string} = ?"
            return query
        else:
            return query

class Object:
    def __init__(self, table):
        self.table = table
        self.query = QueryBuilder(self.table)

    def edit(self, anchor, edit_information):
        query = self.query.edit(edit_information[0], anchor[0])
        print(f"Query : {query}")
        values = [anchor[1], edit_information[1]]
        values = tuple(values)
        executor(query, value)

    def fetch_columns(self, columns):
        query = self.query.instance(columns="*")
        fetch = executor(query)
        return fetch
    
    def delete(self, target):
        pass

