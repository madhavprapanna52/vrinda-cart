"""
Central Executor for running query and data flow
"""
from QueryBuilder import *
import sqlite3 as sql 
from queue import Queue
import os

class Executor:
    def __init__(self):
        self.path = os.getenv("DB_LINK")
        self.tasks = Queue(maxsize=10)

    def run(self):
        connection = sql.connect(self.path)
        cursor = connection.cursor()

        while True:
            task = self.tasks.get()

            query = task.query
            data = task.data

            try:
                cursor.execute(query, data)
                connection.commit()
                print(f"Query Executed")
                return True

            except Exception as e:
                connection.rollback()
                print(f"Exception rasied as : {e}")
