"""
Central Executor for running query and data flow
"""
from DB.QueryBuilder import *
import sqlite3 as sql 
from queue import Queue
import os

class Executor:
    def __init__(self):
        self.path = os.getenv("DB_LINK")
        self.tasks = Queue(maxsize=10)

    def run(self):

        while True:

            task = self.tasks.get()
            print(f"Task Fetched as : {task}")

            query = task.query
            data = task.data
            with sql.connect(self.path) as connection:
                cursor = connection.cursor()

                try:
                    print(f"Final DB-LINK : {query} with Data | {data}")
                    cursor.execute(query, data)
                    connection.commit()
                except Exception as e:
                    print(f"Exception Rasied at Executor : {e}")

