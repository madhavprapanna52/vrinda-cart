"""
Executor
Central Execution flow for all DB requests
Taking taks and Doing them to deliver results
"""
from queue import Queue
import sqlite3 as sql
from dataclasses import dataclass
from typing import Tuple, Any
#import config

# Task Data Model
'''
    Used for Objectified task model which would be used for making task
    and using their dataflow to execute and log information
'''

@dataclass
class Task:
    query_type: str
    table: str
    columns: Tuple[str, ...]
    values: Tuple[Any, ...]  # INFO : serialise multiple data vrinda-carta external loops


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
    def __init__(self, path):
        self.connection_file = path
        self.order = Queue(maxsize=10) # Limmiting test

    def add(self, task):
        self.order.put(task)

    def run(self):
        connection = sql.connect(self.connection_file)
        cursor = connection.cursor()

        while True:
            task = self.order.get() # Taking task from queue
            try:
                query = build_query(task.query_type, task.table, task.columns)
                #log.info(f"Final Query for DB call : {query}")
                cursor.execute(query, task.values)
                connection.commit()

            except Exception as e:
                connection.rollback()
                #log.warning(f" [Failed] Exector failed with Error : {e}")
            finally:
                self.order.task_done()
