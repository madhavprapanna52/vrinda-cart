"""
Central Executor for running query and data flow
"""
from DB.QueryBuilder import *
import sqlite3 as sql 
from queue import Queue
import os


'''
Executor Working
Used for Making Execution of query at paralell threading
 + Dont use at Non deaemon thread as its task could take mili seconds to execute
 + Works to make the write operations for the final tasks
'''
class Executor:
    def __init__(self):
        self.path = os.getenv("DB_LINK")
        self.tasks = Queue()

    def run(self):

        while True:

            task = self.tasks.get()
            query = task.query
            data = task.data
            with sql.connect(self.path) as connection:
                cursor = connection.cursor()

                try:
                    cursor.execute(query, data)
                    connection.commit()
                    task.status = "Done"
                except Exception as e:
                    print(f"Exception Occured as : {e}")
                    task.status = "failed"

