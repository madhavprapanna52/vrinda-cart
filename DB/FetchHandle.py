import sqlite3 as sql
import os

class Fetch:
    def __init__(self):
        self.path = os.getenv("DB_LINK") 

    def filter(self, query, data):
        with sql.connect(self.path) as connection:
            cursor = connection.cursor()
            print(f"Debug data before execution as {query} with data : {data}")
            cursor.execute(query, data)
            info = cursor.fetchall()
            return info  # information fetched with execution

    def instance(self, query):
        with sql.connect(path) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result  # simple instance fetch now 


