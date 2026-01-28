"""
Executor
Central Execution flow for all DB requests
Taking taks and Doing them to deliver results
"""
from queue import Queue
import sqlite3 as sql
from dataclasses import dataclass
from typing import Tuple, Any

# Task Data Model
'''
    Used for Objectified task model which would be used for making task
    and using their dataflow to execute and log information
'''

@dataclass
class Task:
    qt: str
    table: str
    columns: Tuple[str, ...]
    values: Tuple[Any, ...]  # INFO : serialise multiple data via external loops

def build_query(q_type:str, table:str, columns:tuple):
    '''
        Makes simple query for Execution
    q_type list to evaluate and feature
    insertion query : i
    update query : u
    delete : d

    INFO : Load loops for mass execution and these would handle row based insertions for now :)
    '''
    cols = ", ".join(columns)  # Columns string
    placeholders = ", ".join(["?"] * len(columns)) # placeholder string
    query = ""  # default and error results blank
    if q_type == "i": 
        query = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
    if q_type == "u":
        query = f"UPDATE {table} set ({cols}) = ({placeholders})"
    return query  # Expand for other options


class Executor:
    '''
        Central Query Executing system
    inputs : query_type, task
    output : None if operative query or results if fetch query initiated
    '''
    def __init__(self, connection_file):
        self.connection_file = connection_file
        self.order = Queue(maxsize=10) # Limmiting test
        print(f"Order Queue ~ {self.order}")

    def add(self, task):
        self.order.put(task)
        print(f"order Now {self.order}")
        print(f"Task is Added to the executor as {task}")

    def run(self):
        connection = sql.connect(self.connection_file)
        cursor = connection.cursor()

        while True:
            task = self.order.get() # Taking task from queue
            print("I am running +u+")
            try:
                query = build_query(task.qt, task.table, task.columns)
                print(f"Final Query : {query}")
                cursor.execute(query, task.values)
                connection.commit()

            except Exception as e:
                connection.rollback()
                print(f"Query failed with : {e}")
            finally:
                self.order.task_done()
                print(f"Order Now after task done : {self.order}")




        

