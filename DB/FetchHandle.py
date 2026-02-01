import sqlite3 as sql
import os

class Fetch:
    def __init__(self):
        self.path = os.getenv("DB_LINK") 

    def filter(self, query, data):  # INFO : Include with inbuilt QueryBuilder for Making fetch request
        with sql.connect(self.path) as connection:
            cursor = connection.cursor()

            try:
                print(f"Fetch request : {query} ||| {data}")
                cursor.execute(query, data)
                return True, cursor.fetchall()

            except Exception as e:
                print(f"Exception at fetch {e} ")
                return False, []

    def instance(self, query):
        with sql.connect(path) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result  # simple instance fetch now 


